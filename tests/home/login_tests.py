
#from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.checkstatus import CheckStatus

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classLevelSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_ValidLogin", result2, "Some problem with test_Valid Login")


    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):

        #self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "353abcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, " Login is unsuccessfull")
