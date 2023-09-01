import pytest
import self
from pytest_selenium import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\Users\Ярик\PycharmProjects\pytest-selenium\test_selenium_simple\chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.title_contains, "PetFriends"))
   )
   yield

   pytest.driver.quit()

def test_show_my_pets():
    pytest.driver.find_element_by_id('email').send_keys('cerber19912@gmail.com')
    pytest.driver.find_element_by_id('pass').send_keys('Cnhjbntkm4556')
    pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.title_contains, "PetFriends"))
    )

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]')
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]')
    descriptions = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

class element_has_css_class(object):
        def __init__(self, locator, css_class):
            self.locator = locator
            self.css_class = css_class