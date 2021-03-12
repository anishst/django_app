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


    def test_create_category(self):
        category1 = Category.objects.create(name="Test")
        print(category1.name)
    
    def test_create_post(self):
        pass
        # TODO not working using user in post
        # print(self.user.id)
        # newuser = User(2,username="Foo").save()
        # post1 = Post.objects.create(title="Blog Title", body="Body Text", created_on=timezone.now(), category=category1, author=newuser.id)
        # print(post1)

   