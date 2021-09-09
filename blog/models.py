from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    subtitle = models.CharField(max_length=1000,default="")
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='post_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})
        
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)