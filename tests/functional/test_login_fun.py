import pytest

from pages.login_page import LoginPage


def test_negative_with_empty_input(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.click_login()
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_close_error_message(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.click_login()
    login_page.close_error_message()
    assert login_page.get_error_message() == "", "Проверка, что текст ошибки не вернулся"

def test_login_without_password(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.click_login()
    assert login_page.get_error_message() == "Epic sadface: Password is required"


