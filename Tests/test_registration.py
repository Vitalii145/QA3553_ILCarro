from Pages.registration_page import RegistrationPage
from models.users import User


def rest_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        "Nina",
        "Molly",
        "tony@mail.com",
        "password456%"
    )
    registration_page.open_registration_form()
    registration_page.fill_registration_form()
    registration_page.check_policy()
    registration_page.submit_registration()


    assert registration_page.confirmation_text() =="Registered"
    assert registration_page.confirmation_text_1() =="You are logged in success"
    registration_page.close_window()
