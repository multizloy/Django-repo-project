from store.models import Item


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get("session_key")

        # If the user is new, no session key! Create one!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Lets make sure cart is available on all pages of site
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)

        # Logic
        if item_id in self.cart:
            pass

        else:
            self.cart[item_id] = {"price ": str(item.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_item(self):
        # GEt ids form cart
        item_ids = self.cart.keys()
        # USe ids to lookup items in database model
        items = Item.objects.filter(id__in=item_ids)
        # return those looked up items
        return items

    def delete(self, item):
        item_id = str(item)
        # удалить с корзины
        if item_id in self.cart:
            del self.cart[item_id]

        self.session.modified = True
