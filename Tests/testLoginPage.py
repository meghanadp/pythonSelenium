import allure
from webdriver_manager.core import driver

from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.testBase import BaseTest


class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        # create object for loginPage
        self.loginPage = LoginPage(self.driver)

        flag = self.loginPage.is_signup_link_visible()  # return type is boolean
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.Login_Page_Title)
        assert title == TestData.Login_Page_Title

    def test_login(self):
        with allure.step('Do Login with valid credentials'):
          self.loginPage = LoginPage(self.driver)
          self.loginPage.do_login(TestData.User_Name, TestData.Password)
