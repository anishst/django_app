from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


# Class view

class HomeView(ListView):

    # define which model to use
    model = Post
    template_name = 'home.html'

    # sortying by created on field; desc order
    def get_queryset(self):
        return Post.objects.order_by('-created_on')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog_add.html'
    fields = '__all__'  # put all fields on page
    # spcifify fields
    # fields = ('title', 'body') # put specific fields    