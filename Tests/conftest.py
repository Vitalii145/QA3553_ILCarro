import pytest
from selenium import webdriver

from Pages.login_page import Login_Page
from data.User_data import existing_user


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://icarro-v1.netlify.app/login")

    yield driver
    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    login_page = Login_Page(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()
    login_page.close_window()

    return driver