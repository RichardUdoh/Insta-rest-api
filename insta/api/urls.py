from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView,
    like_post

)

app_name = 'api'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('like/', like_post, name="like-post")
]