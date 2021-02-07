from django.urls import path
from .views import PostListView, PostDetailView, AddPostView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail_view'),
    path('add_post/', AddPostView.as_view(), name='add_post_view'),
]
