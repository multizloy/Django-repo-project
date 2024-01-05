from django.shortcuts import render
from .models import Post
from .serializers import Post_Serializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.


def Posts(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = Post_Serializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = Post_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
