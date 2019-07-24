from django.urls import path
from .views import (
    BlogPostRudView,
    BlogPostCreateView,
    BlogPostListView,
    BlogPostRetrieveUpdateView,
    BlogPostRetrieveDestroyView
)

urlpatterns = [
    # api app url
    path('api/post/<int:pk>/', BlogPostRudView.as_view(), name='post_rud'),
    path('api/post/', BlogPostCreateView.as_view(), name='post_create'),
    path('api/post/list/', BlogPostListView.as_view(), name='post_list'),
    path(
        'api/post/update/<int:pk>/',
        BlogPostRetrieveUpdateView.as_view(),
        name='post_update'
    ),
    path(
        'api/post/delete/<int:pk>/',
        BlogPostRetrieveDestroyView.as_view(),
        name='post_delete'
    ),
]
