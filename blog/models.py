from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    feature_image = models.ImageField(upload_to='feature_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.feature_image and hasattr(self.feature_image, 'url'):
            return self.feature_image.url


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
