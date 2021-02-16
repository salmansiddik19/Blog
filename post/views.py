from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_menu'] = Category.objects.all()
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail_view', args=[str(pk)]))


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'category': cats.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_list': category_list})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if total.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['likes_count'] = total.total_likes()
        context['category_list'] = Category.objects.all()
        context['liked'] = liked
        return context


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail_view', kwargs={'pk': self.object.post.id})


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_comment.html'
    fields = '__all__'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list_view')
