from pages.home_page import BasePage


def test_login():
    page = BasePage(driver)
    page.open("http://localhost/opencart/")
    assert "Your Store" in driver.title