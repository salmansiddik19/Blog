from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ('-id')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list_view')
