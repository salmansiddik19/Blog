from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
