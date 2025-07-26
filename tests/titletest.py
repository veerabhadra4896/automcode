from pages.home_page import BasePage


def test_title(driver):
    page = BasePage(driver)
    page.open("http://localhost/opencart/upload/")
    assert "Your Store" in driver.title
