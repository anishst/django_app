from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Category
from blog.forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})
def CategoryView(request, cats):
    # query to get items by category
    category_posts = Post.objects.filter(category_id=cats)
    category_name = Category.objects.filter(id=cats).first()
    return render(request, 'categories.html', {'category_name': category_name, 'category_posts': category_posts})

def LikeView(request, pk):
    # get post using form value 
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    # redirect to same page
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

    


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

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'  # put all fields on page
    template_name = 'blog_add_category.html'  

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