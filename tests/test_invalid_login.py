from pages.login_page import LoginPage

def test_invalid_login(driver):
    login = LoginPage(driver)

    login.login("standard_user", "abc123")

    assert login.get_error_message() == "Epic sadface: Username and password do not match any user in this service"