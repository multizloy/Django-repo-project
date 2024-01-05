from django.urls import path

# from .views import Posts, posts_detail
# from .views import Posts_APIView, Post_Detail_APIView, generic_APIView
from .views import generic_APIView

# app_name = "rest_api"

urlpatterns = [
    # path("posts/", Posts, name="posts"),
    # path("post_detail/<int:pk>/", posts_detail),
    # path("postsAPiView/", Posts_APIView.as_view()),
    # path("detailApiView/<int:pk>/", Post_Detail_APIView.as_view()),
    path("posts/<int:id>/", generic_APIView.as_view()),
]
