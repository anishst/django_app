from django.urls import reverse, resolve
from ..models import Post, User, Category
from ..views import HomeView, PostDetailView, AddPostView
import pytest
# ------------------------------------------------
#                   UNIT TESTS
#  run options: 
#   ptest: pytest -v -s blog/tests/test_urls.py::TestUrls
# -----------------------------------------------

@pytest.mark.unit_tests
@pytest.mark.url_tests
class TestUrls():

    def test_url_for_homepageview_using_view_classname(self):
        url = reverse('home')
        assert resolve(url).func.view_class == HomeView

    #   test using name of view
    def test_url_for_homepageview_using_viewname(self):
        url = reverse('home')
        assert resolve(url).view_name == 'home'


    def test_url_for_postdetailview_using_viewname(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        assert resolve(url).view_name == 'post-detail'

    def test_url_for_addpostview_using_viewname(self):
        url = reverse('add_post')
        assert resolve(url).view_name == 'add_post'

    def test_url_for_postedit_using_viewname(self):
        url = reverse('post-edit',kwargs={'pk': 1})
        assert resolve(url).view_name == 'post-edit'