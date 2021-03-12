from django.test import RequestFactory
from django.urls import reverse
from ..views import HomeView, PostDetailView, AddPostView
from django.contrib.auth.models import User
from mixer.backend.django import mixer
import pytest
# ------------------------------------------------
#                   UNIT TESTS
#  run options: 
#   ptest: pytest -v -s blog/tests/test_views.py::TestViews
# -----------------------------------------------

@pytest.mark.django_db
@pytest.mark.unit_tests
@pytest.mark.view_tests
class TestViews():

    def test_home_view_authenticated(self):
        pass
        # NOT WORKING
        # path = reverse('home')
        # request = RequestFactory().get(path)
        # request.user = mixer.blend(User)

        # response = HomeView(request)
        # assert response.status_code == 200

   