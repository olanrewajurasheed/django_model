from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,related_name='blog_posts')
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-Created_date']

    def __str__(self):
        return self.Title
