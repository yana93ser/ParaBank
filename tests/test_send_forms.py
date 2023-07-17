import allure

from pages.send_forms import Send_Forms
from pages.users import test_user


@allure.tag("UI test")
@allure.title('Проверка формы обратной связи с банком.')
def test_send_forms():
    send_forms = Send_Forms()

    with allure.step("Открыть страницу банка."):
        send_forms.open_page()
    with allure.step("Перейти на форму обратной связи с банком."):
        send_forms.send_email()
    with allure.step("Заполнить форму связи с банком."):
        send_forms.type_email_forms(test_user)
    with allure.step("Отправить форму."):
        send_forms.send_forms()
