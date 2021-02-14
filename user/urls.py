from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_success', views.password_success, name='success_password'),
    path('<int:pk>/profile', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(),
         name='create_profile_page'),
]
