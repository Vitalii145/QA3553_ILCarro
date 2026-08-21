from selenium import webdriver
from Pages.login_page import Login_Page

VALID_EMAIL = 'meizum3s17@gmail.com'
VALID_PASSWORD = 'Citrus123@'
INVALID_EMAIL = 'meizumsdf@gmail.com'
INVALID_PASSWORD = 'Citrus56754@'

def test_login_success(driver):
    login_page = Login_Page(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()


def test_login_wrong_email(driver):
    login_page = Login_Page(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.error_message_text()=="Wrong email format"
    assert login_page.submit_button_disabled()


def test_login_empty_email(driver):
    login_page = Login_Page(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.error_message_text()=="Email is required"
    assert login_page.submit_button_disabled()

def test_login_wrong_password(driver):
    login_page = Login_Page(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.confirmation_text()=="Login failed"
    assert login_page.confirmation_text_1()=='"Login or Password incorrect"'

def test_login_empty_password(driver):
    login_page = Login_Page(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("")
    login_page.submit_login()

    assert login_page.error_message_text()=="Password is required"
    assert login_page.submit_button_disabled()