from dataclasses import dataclass


@dataclass
class Users:
    name: str
    email: str
    phone: str
    message: str


test_user = Users(
    name='Test',
    email='test@mail.ru',
    phone='123456789',
    message='Ввести любое сообщение для банка.'
)


@dataclass
class NewUsers:
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone: str
    ssn: str
    user_name: str
    password: str
    confirm: str


test_new_user = NewUsers(
    first_name='Test',
    last_name='Testov',
    address='Address',
    city='City',
    state='State',
    zip_code='1234',
    phone='123456789',
    ssn='9875321',
    user_name='test_user_ya',
    password='1234',
    confirm='1234'
)


@dataclass
class LoginUsers:
    user_name: str
    password: str


test_login_user = LoginUsers(
    user_name='test_user_ya',
    password='1234'
)
