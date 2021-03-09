
from django.urls import path
from .views import HomeView, PostDetailView, AddPostView

urlpatterns = [
    # path('', views.HomeView, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]