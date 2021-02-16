from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
    CategoryListView,
    LikeView,
    AddCommentView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail_view'),
    path('add_post', AddPostView.as_view(), name='add_post_view'),
    path('add_category', AddCategoryView.as_view(), name='add_category_view'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='edit_post_view'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
]
