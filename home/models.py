from django.db import models
from django.utils import timezone

# Create your models here.
class Contacts(models.Model):
    # post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    # comment_date = models.DateTimeField(default=timezone.now)

class comments(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.png', upload_to='comment_pic')
    date_posted = models.DateTimeField(default=timezone.now)
    position = models.CharField(max_length=100, null=True)