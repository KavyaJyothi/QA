from  appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium import  webdriver
from  traceback import  print_stack

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return MobileBy.ID
        elif locatorType == "class":
            return MobileBy.CLASS_NAME
        elif locatorType == "xpath":
            return MobileBy.XPATH

        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType=id):
        element=None
        try:
            element = self.getElement(locator, locatorType)
            result=element.is_displayed()
            if result:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
    def sendKeys(self, data,locator, locatorType="id"):
        element=None
        try:
            element = self.getElement(locator, locatorType)

            element.send_keys(data)
            print("Data sent on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot find element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

