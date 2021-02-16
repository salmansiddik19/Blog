from django.shortcuts import render, get_object_or_404
from django.views import generic
from post.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, ChangePasswordForm, ProfilePageForm


class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_user_profile.html'
    success_url = reverse_lazy('post_list_view')
    # fields = ['bio', 'profile_picture']


class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_page = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile_page'] = profile_page
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post_list_view')

    def get_object(self):
        return self.request.user


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('success_password')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
