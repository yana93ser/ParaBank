from selene import be
from selene.support.shared import browser

from pages.users import Users, NewUsers, LoginUsers


class SendForm:

    def send_email(self):
        browser.element('[href="contact.htm"]').press_enter()
        return self

    def type_email_forms(self, user: Users):
        browser.element('#name').type(user.name)
        browser.element("#email").type(user.email)
        browser.element("#phone").type(user.phone)
        browser.element('#message').type(user.message)
        return self

    def send_forms(self):
        browser.element('[value="Send to Customer Care"]').press_enter()
        browser.element('#rightPanel').should(be.visible)
        return self



class RegisterForm:

    def register(self):
        browser.element('[href="register.htm"]').press_enter()
        return self

    def type_register_form(self, new_user: NewUsers):
        browser.element('#customer\.firstName').type(new_user.first_name)
        browser.element('#customer\.lastName').type(new_user.last_name)
        browser.element('#customer\.address\.street').type(new_user.address)
        browser.element('#customer\.address\.city').type(new_user.city)
        browser.element('#customer\.address\.state').type(new_user.state)
        browser.element('#customer\.address\.zipCode').type(new_user.zip_code)
        browser.element('#customer\.phoneNumber').type(new_user.phone)
        browser.element('#customer\.ssn').type(new_user.ssn)
        browser.element('#customer\.username').type(new_user.user_name)
        browser.element('#customer\.password').type(new_user.password)
        browser.element('#repeatedPassword').type(new_user.password)
        return self

    def send_form(self):
        browser.element('[value="Register"]').press_enter()
        return self

    def account_was_created(self):
        browser.element('#rightPanel').should(be.visible)
        return self


class LoginForm:

    def type_login_form(self, login_user: LoginUsers):
        browser.element('[name="username"]').type(login_user.user_name)
        browser.element('[name="password"]').type(login_user.password)
        return self
    def send_login(self):
        browser.element('[value="Log In"]').press_enter()
        return self
