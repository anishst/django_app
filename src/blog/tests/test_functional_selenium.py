from selenium import webdriver
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
    