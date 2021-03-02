"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def about_user(**kwargs):
    print(f"1: Пользователь: {kwargs}")


about_user(имя="Джон", фамиия="Смит", год=1985, email="Джон@Смит", город="Иваново", телефон=89009990000)


def profile(el_1, el_2, el_3, el_4, el_5, el_6):
    return ' '.join([el_1, el_2, el_3, el_4, el_5, el_6])


print("2:", profile(el_1='Ivan', el_2='Ivanov', el_3='01.01.2000', el_4='Ivanovo', el_5='ivanov@ivan',
                    el_6='8-999-01-01-200'))


def user(**kwargs):
    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"3: {name} {surname} {birth_year} года рождения, в городе {city}. \n   Контакты: {email}, {phone} "


print(user(name='Анна', surname='Иванова', birth_year=1990, city='Москва', email='d@d', phone=3444556677889))
_____________________________
1: Пользователь: {'имя': 'Джон', 'фамиия': 'Смит', 'год': 1985, 'email': 'Джон@Смит', 'город': 'Иваново', 'телефон': 89009990000}
2: Ivan Ivanov 01.01.2000 Ivanovo ivanov@ivan 8-999-01-01-200
3: Анна Иванова 1990 года рождения, в городе Москва. 
   Контакты: d@d, 3444556677889 
 
