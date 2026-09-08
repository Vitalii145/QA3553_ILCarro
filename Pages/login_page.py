import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Base_Page import BasePage


class Login_Page(BasePage):
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_YALLA = (By.CSS_SELECTOR, 'button[class="btn btn--primary"]')
    BUTTON_LOG_OUT = (By.XPATH, "//button[text()='Log out']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p")
    OK_BTN = (By.XPATH, "//*[text()='OK']")


    def open_login_form(self):
        self.click(self.LOGIN_NAV_LINK)
        time.sleep(2)

    def fill_email(self, email):
        self.fill(*self.EMAIL_PLACEHOLDER)

    def fill_password(self, password):
        self.fill(*self.PASSWORD_PLACEHOLDER)

    def submit_login(self):
        self.click(self.BUTTON_YALLA)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def confirmation_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text

    def confirmation_message(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE))
        return element.text

    def close_window(self):
        self.click(self.OK_BTN)

    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.BUTTON_LOG_OUT)
            )
            return True
        except TimeoutException:
            return False

    def error_message_text(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def submit_button_disabled(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.BUTTON_YALLA)
        )
        return element.get_attribute("disabled") is not None