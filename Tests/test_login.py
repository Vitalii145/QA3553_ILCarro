from selenium import webdriver
from Pages.login_page import Login_Page

VALID_EMAIL = 'meizum3s17@gmail.com'
VALID_PASSWORD = 'Citrus123@'

def test_login_success(driver):
    login_page = Login_Page(driver)

    # login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()