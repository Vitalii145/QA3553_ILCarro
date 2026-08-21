import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:

    NAV_REGISTR_BTN = (By.CSS_SELECTOR, "[href='/register']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    YALLA_BTN = (By.XPATH, "//*[text()='Y'alla!']")
    CHECK_BOX = (By.XPATH, "//*[text()='Y']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    CONFIRMATION_TEXT_1 = (By.CSS_SELECTOR, "p")
    OK_BTN = (By.XPATH, "//*[text()='OK']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_form(self):
        self.driver.find_element(*self.NAV_REGISTR_BTN).click()
        time.sleep(2)

    def confirmation_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text

    def confirmation_text_1(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT_1))
        return element.text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()



    def fill_registration_form(self,user):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)
