
from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('', views.HomeView, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="post-delete"),
]