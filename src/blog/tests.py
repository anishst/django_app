from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import Post, User, Category
from blog.views import HomeView, PostDetailView, AddPostView

# Create your tests here.


# models test
# ------------------------ RESOURCES ---------------------------------------------------------------------#

    #https://docs.djangoproject.com/en/3.1/intro/tutorial05/#introducing-automated-testing
    # https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#types-of-tests
    # https://www.youtube.com/watch?v=0MrgsYswT1c

# # ------------------------ RESOURCES -----------------------------------------------------------------------#
# class BlogModelTest(TestCase):

#     # def create_whatever(self, title="only a test", body="yes, this is only a test", author="admin"):
#     #     return Post.objects.create(title=title, body=body, created_on=timezone.now(), author=author)

#     def test_category_creation(self):
#         new_cat =Category.objects.create(name="New Category Test")
#         print(new_cat.name)
#         assert new_cat.name == 'New Category Test'


# urls test
class TestUrls(SimpleTestCase):

    def test_homepageview_is_displayed(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)


    def test_postdetailview_is_displayed(self):
        url = reverse('post-detail', args=['2'])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)


    def test_addpostview_is_displayed(self):
        url = reverse('add_post')
        self.assertEquals(resolve(url).func.view_class, AddPostView)