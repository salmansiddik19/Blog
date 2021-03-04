from django.db import models
from django.contrib.auth.models import User


class UserParent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    def __str__(self):
        return self.father_name
