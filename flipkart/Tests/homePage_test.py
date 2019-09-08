from Pages.home_page import HomePage
from selenium import  webdriver
import unittest
import pytest
import  time

@pytest.mark.usefixtures("setUp")
class HomePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):

        self.hp = HomePage(self.driver)



    def test_search(self, data="iphone"):
        self.hp.searchForAnItem("iphone")
        time.sleep(5)




