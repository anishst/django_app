from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    #   return user to detail page when form is submitted
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')