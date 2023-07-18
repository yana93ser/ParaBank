import allure

from pages.send_form import SendForm, RegisterForm
from pages.users import test_user, test_new_user


@allure.tag("UI test")
@allure.title('Проверка формы обратной связи с банком.')
def test_send_form():
    send_form = SendForm()

    with allure.step("Открыть страницу банка."):
        send_form.open_page()
    with allure.step("Перейти на форму обратной связи с банком."):
        send_form.send_email()
    with allure.step("Заполнить форму связи с банком."):
        send_form.type_email_forms(test_user)
    with allure.step("Отправить форму."):
        send_form.send_forms()


def test_regisret_form():
    register_form = RegisterForm()
    with allure.step("Открыть страницу банка."):
        register_form.open_page()
    with allure.step("Перейти на форму регистрации."):
        register_form.register()
    with allure.step("Заполнить форму регистрации."):
        register_form.type_register_form(test_new_user)
    with allure.step("Отправить форму."):
        register_form.send_form()
    with allure.step("Проаерить что аккаунт создан."):
        register_form.account_was_created()
