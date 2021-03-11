
from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    # path('', views.HomeView, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="post-delete"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<int:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='post-like'),
]