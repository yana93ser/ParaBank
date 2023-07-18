import allure
from selene.support.shared import browser

from pages.send_form import SendForm, RegisterForm, LoginForm
from pages.users import test_user, test_new_user, test_login_user


@allure.tag("UI test")
@allure.title('Проверка формы обратной связи с банком.')
def test_send_form(setup_browser):
    send_form = SendForm()
    browser.open('/')
    with allure.step("Перейти на форму обратной связи с банком."):
        send_form.send_email()
    with allure.step("Заполнить форму связи с банком."):
        send_form.type_email_forms(test_user)
    with allure.step("Отправить форму."):
        send_form.send_forms()


@allure.tag("UI test")
@allure.title('Проверка формы регистрации нового пользователя.')
def test_regisret_form():
    register_form = RegisterForm()
    browser.open('/')
    with allure.step("Перейти на форму регистрации."):
        register_form.register()
    with allure.step("Заполнить форму регистрации."):
        register_form.type_register_form(test_new_user)
    with allure.step("Отправить форму."):
        register_form.send_form()
    with allure.step("Проверить что аккаунт создан."):
        register_form.account_was_created()


@allure.tag("UI test")
@allure.title('Проверка формы авторизации пользователя.')
def test_login():
    login_form = LoginForm()
    browser.open('/')
    with allure.step("Заполнить форму авторизации."):
        login_form.type_login_form(test_login_user)
    with allure.step("Отправить форму."):
        login_form.send_login()
