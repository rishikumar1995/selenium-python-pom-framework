from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


