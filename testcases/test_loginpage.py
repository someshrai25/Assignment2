
from pages.PIMPage import PagePIM
from pages.loginPage import LoginPage
from packageutilities.BaseClass import BaseClass
from pages.adminpage import AdminPage

class TestLogin(BaseClass):

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.login("Admin","admin123")

    def test_user_search(self):
        ap = AdminPage(self.driver)
        ap.userSearch("Admin")
        result = ap.verifySuccessfulSearch()
        assert result == True

    def test_invalid_search(self):
        invalid = AdminPage(self.driver)
        invalid.invalidSearch("sfsdfd")

    def test_PIM_Page(self):
        addUser = PagePIM(self.driver)
        addUser.click_PIM("New", "User")