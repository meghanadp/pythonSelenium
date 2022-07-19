import allure
import pytest
from selenium.webdriver.common.by import By

from Config.Config import TestData
from Pages.BasePage import BasePage


# BasePage class is super class of all Pages
from Tests import Report



class LoginPage(BasePage):
    """By locators"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    # constructor for this page
    def __init__(self, driver):
        super().__init__(driver)
    # Super keyword will be used to call constructor of super class
        self.driver.get(TestData.Base_Url)

    """Page actions"""

    # this is used to get title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # used to check sign up is visible or not
    def is_signup_link_visible(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        Report.report_step('Enter username')
        self.do_send_keys(self.EMAIL, username)
        Report.report_step('Enter password')
        self.do_send_keys(self.PASSWORD, password)
        Report.report_step('Click on Login Button')
        self.do_click(self.LOGIN_BUTTON)
