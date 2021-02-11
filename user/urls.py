from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_success', views.password_success, name='success_password'),
]
