# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class Login_Page:
#     LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
#     EMAIL_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='username']")
#     PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='password']")
#     BUTTON_YALLA =(By.CSS_SELECTOR,'button[class="btn btn--primary"]')
#     BUTTON_LOG_OUT = (By.XPATH, "//button[text()='Log out']")
#
#     def __init__(self, driver,timeout=10):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, timeout)
#
#     def _find(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator))
#
#     def open_login_form(self):
#         self.driver.find_element(*self.LOGIN_NAV_LINK).click()
#
#     def fill_email(self, email):
#         self.driver.find_element(*self.EMAIL_PLACEHOLDER).clear()
#         self.driver.find_element(*self.EMAIL_PLACEHOLDER).send_keys(email)
#
#     def fill_password(self, password):
#         self.driver.find_element(*self.PASSWORD_PLACEHOLDER ).clear()
#         self.driver.find_element(*self.PASSWORD_PLACEHOLDER ).send_keys(password)
#
#
#     def submit_login(self):
#         self.driver.find_element(*self.BUTTON_YALLA).click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_YALLA = (By.CSS_SELECTOR, 'button[class="btn btn--primary"]')
    BUTTON_LOG_OUT = (By.XPATH, "//button[text()='Log out']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def open_login_form(self):
        self._find(self.LOGIN_NAV_LINK).click()

    def fill_email(self, email):
        field = self._find(self.EMAIL_PLACEHOLDER)
        field.clear()
        field.send_keys(email)

    def fill_password(self, password):
        field = self._find(self.PASSWORD_PLACEHOLDER)
        field.clear()
        field.send_keys(password)

    def submit_login(self):
        self._find(self.BUTTON_YALLA).click()