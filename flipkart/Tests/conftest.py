import os
from  appium import webdriver
import pytest
from appium.webdriver.webdriver import WebDriver


@pytest.yield_fixture(scope="class")
def setUp(request):
    flipkart_path=os.path.abspath("/home/kavya/tools/Flipkart.apk")
    desired_cap={
          "platformName": "Android",
          "platformVersion": "8.0.0",
          "deviceName": "android",
          "app": flipkart_path,
          "appPackage": "com.flipkart.android",
          "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
          "noReset": True
    }
    driver: WebDriver= webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)

    request.cls.driver = driver
    yield driver
    #driver.quit()