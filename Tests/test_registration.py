import random
import uuid

from Pages.registration_page import RegistrationPage
from data.User_data import create_user
from models.users import User


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    user = create_user()


    registration_page.open_registration_form()
    registration_page.fill_registration_form()
    registration_page.check_policy()
    registration_page.submit_registration()


    assert registration_page.confirmation_text() =="Registered"
    assert registration_page.confirmation_message() =="You are logged in success"
    registration_page.close_window()

def rest_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(name = "")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()


    assert registration_page.error_message_text() =="Nam is registered"
    assert registration_page.confirmation_message() =="You are logged in success"
    registration_page.close_window()