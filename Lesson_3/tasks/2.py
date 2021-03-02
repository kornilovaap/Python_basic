"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def about_user(**kwargs):
    print(f"1: Пользователь: {kwargs}")


about_user(имя="q", фамиия="a", год=12, email="w", город="qw", телефон=12)


def profile(el_1, el_2, el_3, el_4, el_5, el_6):
    return ' '.join([el_1, el_2, el_3, el_4, el_5, el_6])


print("2:", profile(el_1='Ivan', el_2='Ivanov', el_3='01.01.2000', el_4='Ivanovo', el_5='ivanov@ivan.org',
              el_6='8-999-01-01-200'))


def user(**kwargs):
    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"3: {name} {surname} {birth_year} года рождения, в городе {city}. \nКонтакты: {email}, {phone} "


print(user(name='Анна', surname='Иванова', birth_year=1990, city='Москва', email='d@d', phone=34))
