from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    
    content=models.TextField()
    
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        
        return f"Comment by {self.author} on {self.post}"