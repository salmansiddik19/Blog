from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list_view')


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to='images/profile')

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('post_list_view')


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=255, default='blog')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='posts')

    class Meta:
        db_table = 'posts'

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_list_view')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('post_list_view')
