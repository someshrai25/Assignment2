import time
import pytest
from pages.loginPage import LoginPage
from packageutilities.BaseClass import BaseClass
from pages.adminpage import AdminPage

class TestLogin(BaseClass):

    #@pytest.fixture(autouse=True)
    #def classMethod(self):
    #    self.lp = LoginPage()

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.login("Admin","admin123")

    def test_user_search(self):
        ap = AdminPage(self.driver)
        ap.userSearch("Admin1234567")
        result = ap.verifySuccessfulSearch()
        assert result == True

    def test_invalid_search(self):
        invalid = AdminPage(self.driver)
        invalid.invalidSearch("sfsdfd")
