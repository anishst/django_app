from django.urls import reverse, resolve
from ..models import Post, User, Category
from ..views import HomeView, PostDetailView, AddPostView


class TestUrls():

    def test_homepageview_is_displayed(self):
        url = reverse('home')
        assert resolve(url).func.view_class == HomeView


    def test_postdetailview_is_displayed(self):
        url = reverse('post-detail', args=['2'])
        assert resolve(url).func.view_class == PostDetailView


    def test_addpostview_is_displayed(self):
        url = reverse('add_post')
        assert resolve(url).func.view_class == AddPostView