from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    """" class for region"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """" class for category"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """" class for posts"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    banner_img = models.ImageField(upload_to='post-baner/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    """" class for postimages"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post-img/')


class PostVideo(models.Model):
    """" class for postvideaos"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-video/')
    video_url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    """" class for commentaries"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Contact(models.Model):
    """" class for contacts"""
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name