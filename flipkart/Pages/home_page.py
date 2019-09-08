from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from Base.selenium_driver import SeleniumDriver
import time

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    open_app_again_xpath = "/hierarchy/android.widget.FrameLayout"
    close_app_id = "android:id/aerr_close"
    search_tab_id = "com.flipkart.android:id/search_widget_textbox"
    hamburger_xpath='//android.widget.ImageButton[@content-desc="Open Drawer"]'
    electronics_xpath="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView"
    electronics_list_class='android.widget.TextView'
    def clickOpenApp(self):
        self.elementClick(self.open_app_again_xpath, locatorType="xpath")

    def clickCloseApp(self):
        self.elementClick(self.close_app_id)

    def searchItem(self, data):
        serch_ele=self.driver.find_element_by_id(self.search_tab_id)
        time.sleep(8)
        self.driver.set_value(serch_ele, data)
        self.driver.execute_script("mobile: performEditorAction", {'action': 'search'})

    def scroll_down(self):
        user_action= TouchAction(self.driver)
        for i in range(5):
            user_action.press(x=489,y=1608).move_to(x=489, y=744).release().perform()
            time.sleep(4)
    def click_hamburger(self):
        self.elementClick(self.hamburger_xpath, locatorType="xpath")

    def select_electronics(self):
        self.elementClick(self.electronics_xpath, locatorType="xpath")
    def find_list_of_elements_electronics(self):
        elements_list=self.driver.find_elements_by_class_name(self.electronics_list_class)
        actual_list=[]
        for el in elements_list:
            ele=el.get_attribute('text')
            actual_list.append(str(ele))
        print(actual_list)





    def searchForAnItem(self, data):
        time.sleep(2)
        self.clickOpenApp()
        time.sleep(5)
        self.clickCloseApp()
        time.sleep(5)
        #self.searchItem(data)
        time.sleep(8)
        #self.scroll_down()
        self.click_hamburger()
        time.sleep(6)
        self.select_electronics()
        time.sleep(4)
        self.find_list_of_elements_electronics()


