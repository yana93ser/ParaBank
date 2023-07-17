from selene.support.shared import browser

from pages.users import Users


class Send_Forms:

    def open_page(self):
        browser.open('https://parabank.parasoft.com/parabank/index.htm')
        return self

    def send_email(self):
        browser.element("#headerPanel > ul.button > li.contact > a").press_enter()
        return self

    def type_email_forms(self, user: Users):
        browser.element('#name').type(user.name)
        browser.element("#email").type(user.email)
        browser.element("#phone").type(user.phone)
        browser.element('#message').type(user.message)
        return self

    def send_forms(self):
        browser.element('[value="Send to Customer Care"]').press_enter()
        return self
