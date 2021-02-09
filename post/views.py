from django.shortcuts import render
from django.views import generic
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ('-created_at')


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'category': cats.title(), 'category_posts': category_posts})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list_view')
