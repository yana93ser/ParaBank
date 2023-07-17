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
