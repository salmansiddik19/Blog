from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


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


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=255, default='blog')

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_list_view')
