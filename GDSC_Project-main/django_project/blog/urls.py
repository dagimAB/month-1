from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    UserPostListView
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<int:pk>/posts/', UserPostListView.as_view(), name='user-posts'),
]

urlpatterns = format_suffix_patterns(urlpatterns)