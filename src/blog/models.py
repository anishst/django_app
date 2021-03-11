from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')
class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    #   return user to detail page when form is submitted
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')