from django.db import models
from django.contrib.auth.models import User

 
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    content = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=150)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
