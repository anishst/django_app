## Django


### Setup

1. create virtual env: ```python -m venv venv```
2. activate venv: ```source venv/Scripts/activate```; you can deactivate by: ```deactivate```
3. install packages; 
    - ```pip install django```
    - ```pip freeze``` would show installed packages
4. start main project: ```django-admin.py startproject mysite```; blog is the name I used; if command didn't work try without .py 
5. cd to dir: ```cd mysite```
6. migrate dbs: ```python manage.py migrate```
7. run project: ```python manage.py runserver```
8. open default by going to: http://localhost:8000/
9. stop and create superuser:```winpty python manage.py createsuperuser```; follow command prompts
10. run server and go to: http://localhost:8000/admin; should be able to login as admin. This completes initial setup

### Model creation 3-step process:
  - url 
  - view
  - template file


repeat below for each app directory you want to add:


1. create a blog dir : ```python manage.py startapp blog```
2. add blog under mysite\mysite\settings.py file under INSTALLED_APPS list
3. update mysite\mysite\urls.py
    ```python
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('blog.urls')),
        ]       
    ```

4. Write your first view:```mysite\blog\views.py```
    ```python
    def home(request):
        return render(request, 'home.html', {})
    ```
5. update mysite\blog\urls.py
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.home, name="home"),
    ]
    ```
6. add template html file: mysite\blog\templates\home.html
7. re-run app and you should see home page updated with new home.html page

### Create Blog Post Model
1. create model: mysite\blog\models.py
    ```python
    class Post(models.Model):
        title = models.CharField(max_length=255)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        body = models.TextField()
    
        def __str__(self):
            return self.title + ' | ' + self.author
    ```
2. register model:mysite\blog\admin.py
    ```python
    from django.contrib import admin
    from .models import Post
    
    # Register your models here.
    admin.site.register(Post)
    
    ```
3. migrate new model by running: 
    1. ``` python manage.py makemigrations```
    2. ```python manage.py migrate```
4. run server to see changes and you should be able to manage posts now via admin panel

### Django Shell Command example

1. enter by: ```python manage.py shell```
2. import model ex: ```from blog.models import Post```
3. see all items: ```Post.objects.all().values()```


### Load data using JSON


```json
[
    {
      "title": "My Updated Post",
      "body": "My first updated post!\r\n\r\nThis is exciting!",
      "category": 4,
      "author": 1
    },
    {
      "title": "A Second Post",
      "body": "This is a post from a different user...",
      "category": 4,
      "author": 1
    }
  
  ]
  ```

1. make sure json file is same folder as manage.py
2. bring up shell
3. run below commands one by one; 
```python
from blog.models import Post, Category
from django.utils import timezone
from django.contrib.auth.models import User

with open('posts.json') as f:
	posts_json = json.load(f)
for post in posts_json:
	post = Post(title=post['title'], body=post['body'], created_on=timezone.now(), category=Category(post['category']), author=User(post['author'])) 
	post.save()
```

### [Django Paginator](https://docs.djangoproject.com/en/dev/topics/pagination/)


```python
from django.core.paginator import Paginator
posts = ['1', '2', '3', '4','5']
p = Paginator(posts,2) # 2 posts per page
# see num of pages
p.num_pages
# loop over pages
for page in p.page_range:
    print(page)
# access specific page
p1 = p.page(1) # output: <Page 1 of 3>
# get page number
p1.number # output 1
# get objects on the page
p1.object_list # output: ['1', '2']
# check if prev page
p1.has_previous() # false
p1.has_next() # true
# get next page #
p1.next_page_number() # 2

```
[How to Paginate with Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
### Django Testing

- https://docs.djangoproject.com/en/3.1/topics/testing/tools/
- https://www.youtube.com/watch?v=28zdhLPZ1Zk&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=6

#### Unit Tests
```python

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
```

#### functional Tests
```python

# functional tests
from django.utils import timezone
from selenium import webdriver
from .models import Post, User, Category
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

#  run these usig: python manage.py test tests.test_functional
class TestProjectPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        blog_title = self.browser.find_element_by_tag_name('H1')
        self.assertEquals(blog_title.text, "Blog Posts")

    def test_blog_post_add(self):
        category1 = Category(1,"test1")
        print(f"New category added{category1}")
        #TODO : NOT WORKING: sqlite3.IntegrityError: FOREIGN KEY constraint failed
        post1 = Post.objects.create(title="Blog Title", body="Body Text", created_on=timezone.now(), category=category1, author=User(1,"admin"))
        print(post1)
        self.browser.get(self.live_server_url)
```

## Resources:
- [Django official page](https://www.djangoproject.com/)
- [Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
- Video tutorials
    - [codemy blog app](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
    - [codemy stock app](https://www.youtube.com/watch?v=iu3V4cOJW4I&list=PLCC34OHNcOtqNxahjUPo2BPC2qrVNawYK)
    - [corey](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [VS Code Setup](https://code.visualstudio.com/docs/python/tutorial-django)
- [VS Code plugins](https://morioh.com/p/b6323e6cdfca)
    - [Djaneiro - Django Snippets](https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro)
        - var = {{}}
        - block
- [random text gen](https://www.lipsum.com/)
- Queries
    - [DB Q](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
- Testing
    - [Django Testing Playlist](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
    - [Testing Tools](https://docs.djangoproject.com/en/3.1/topics/testing/tools/)
- Examples:
    - [Blog Example](https://djangocentral.com/building-a-blog-application-with-django/)    
    - [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
    - [cOREY GITHUB](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog)

## KNown issues

1. RuntimeError: Database access not allowed, use the "django_db" mark
fix add marker to pytests