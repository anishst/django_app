from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


# Class view
class HomeView(ListView):

    # define which model to use
    model = Post
    template_name = 'home.html'
    # order by created_on desc order
    ordering = ['-created_on']

    # sortying by created on field; desc order
    # def get_queryset(self):
    #     return Post.objects.order_by('-created_on')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_add.html'
    # fields = '__all__'  # put all fields on page
    # spcifify fields
    # fields = ('title', 'body') # put specific fields    
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_update.html'    
    # fields = ('title', 'body', 'author', 'favorite') # put specific fields 
    # create separate form class if specific fields needed

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog_delete.html' 
    # re-direct to home page
    success_url = reverse_lazy('home')     