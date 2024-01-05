# test 1
# from django.shortcuts import render
# from .models import Post
# from .serializers import Post_Serializer
# from django.http import JsonResponse, HttpResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.


# @csrf_exempt
# def Posts(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = Post_Serializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = Post_Serializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def posts_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = Post_Serializer(post)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = Post_Serializer(post, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         post.delete()
#         return HttpResponse(status=204)

# response and request
# from django.shortcuts import render
# from .models import Post
# from .serializers import Post_Serializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(["GET", "POST"])
# def Posts(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = Post_Serializer(posts, many=True)
#         return Response(
#             serializer.data,
#         )

#     elif request.method == "POST":
#         serializer = Post_Serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def posts_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "GET":
#         serializer = Post_Serializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = Post_Serializer(post, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status=204)

# classed based views
# from django.shortcuts import render
# from .models import Post
# from .serializers import Post_Serializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from django.http import Http404


# class Posts_APIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = Post_Serializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Post_Serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Post_Detail_APIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = Post_Serializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         post = self.get_object(pk)

#         serializer = Post_Serializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, pk, request):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# generic and mixins
from django.shortcuts import render
from .models import Post
from .serializers import Post_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated


class generic_APIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = Post_Serializer
    queryset = Post.objects.all()
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# request and response
# class Posts_APIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = Post_Serializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Post_Serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Post_Detail_APIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = Post_Serializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         post = self.get_object(pk)

#         serializer = Post_Serializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, pk, request):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
