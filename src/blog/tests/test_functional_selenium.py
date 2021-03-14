from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest
import time

#Fixture for drivers
# use params to test multiple browsers
@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "edge":
        web_driver = webdriver.Edge()

    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()

# ****************************************************************************************
#  TESTS  from scr folder: pytest -v -s blog/tests/test_functional_selenium.py
# ****************************************************************************************
@pytest.mark.usefixtures("driver_init")
class TestDjangoApp():

    def test_homepage(self):
        self.driver.get("http://localhost:8000")
        print(self.driver.title)

    def test_add_post(self):
        self.driver.get("http://localhost:8000/add_post")
        print(self.driver.title)

    def test_category_page(self):
        self.driver.get("http://localhost:8000/add_category")
        print(self.driver.title)
        self.driver.find_element_by_name('name').send_keys("New One added via Selenium")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def test_add_new_post(self):
        self.driver.get("http://localhost:8000/add_post")
        print(self.driver.title)
        self.driver.find_element_by_name('title').send_keys("test")
        authour_dd = Select(self.driver.find_element_by_name("author"))
        authour_dd.select_by_visible_text("admin") 
        category_dd = Select(self.driver.find_element_by_name("category"))
        category_dd.select_by_visible_text("Python") 
        # self.driver.find_element_by_name('title').send_keys("test")
        self.driver.find_element_by_name('body').send_keys("body test")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)


    def test_view_post_and_delete(self):
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_link_text("test").click()
        self.driver.find_element_by_link_text("Delete").click()
        self.driver.find_element_by_xpath("//button[@type='submit']").click()