from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    feature_image = models.ImageField(upload_to='feature_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
