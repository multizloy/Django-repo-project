from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Order


@csrf_exempt
def stripe_webhook(request):
    if request.method == "POST":
        payload = request.body
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        if session.mode == "payment" and session.payment_status == "paid":
            try:
                order_id = session.client_reference_id
            except Order.DoesNotExist:
                return HttpResponse(status=404)

            order = Order.objects.get(id=order.id)
            order.paid = True
            order.save()
    return HttpResponse(status=200)
