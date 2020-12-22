from django.urls import path, include
from .views import (
    PostListView
)

app_name = 'api'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]