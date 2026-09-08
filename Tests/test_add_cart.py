
from Pages.add_car_page import AddCarPage
from data.car_data import create_car


def test_add_car_success(authenticated_driver):
    car_work_page =AddCarPage(authenticated_driver)
    car= create_car()

    car_work_page.open_car_form()
    car_work_page.fill_car_form(car)
    car_work_page.submit_car()
