from django.urls import reverse, resolve
from ..models import Post, Category
from ..views import HomeView, PostDetailView, AddPostView
from django.utils import timezone
from django.contrib.auth.models import User
import pytest
# ------------------------------------------------
#                   UNIT TESTS
#  run options: 
#   ptest: pytest -v -s blog/tests/test_models.py::TestModels
# -----------------------------------------------

@pytest.mark.django_db
@pytest.mark.unit_tests
@pytest.mark.model_tests
class TestModels():


    
    def test_create_post(self):
        pass
        # this worked on shell
        # category1 = Category.objects.create(name="Test")
        # Post.objects.create(title="Blog Title", body="Body Text", created_on=timezone.now(), category=Category.objects.create(name="Tes2"), author=User(1))
        # Post.objects.create(title="Blog Title", body="Body Text", created_on=timezone.now(), category=Category.objects.filter(name='Python').first().id, author=User(1)).save()

    # def test_create_category(self):
    #     category1 = Category.objects.create(name="New One")
    #     category1.save()

    # FOR SHELL PROACTICE
    # from blog.models import Post, Category
    # Post.objects.all()
    # Post.objects.all().first()
    # post1 = Post.objects.all().first()
    # post1.id

    # cat1 = Category.objects.filter(name='Python').first()
    # Category.objects.filter(name='Python')
    # cat1.id
    # Category.objects.filter(name='Python').first().id