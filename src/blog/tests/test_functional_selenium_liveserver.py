from django.utils import timezone
from selenium import webdriver
from ..models import Post, User, Category
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

#  run these usig: python manage.py test tests.test_functional
class TestProjectPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        blog_title = self.browser.find_element_by_tag_name('H1')
        self.assertEquals(blog_title.text, "Blog Posts")
        time.sleep(5)
