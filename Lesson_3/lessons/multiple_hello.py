users = ["Anna", "Roma", "Nina", "Dina"]


def say_hello(*user_list):
    # * - любой аргумент, кот будет передан как позиционный, будет записан в качестве вот этого списка
    for user in user_list:
        print(user)


say_hello(*users)

# если у нас есть неограничееное число позиционных аргументов (с помощью * в функции)
# можем ли мы задавать именованные аргументы?
# можем, но чуть сложнее, если мы хотим также неограниченное число аргументов
# вся сложность лишь в том, что надо будет поставить две звездочки, т.е. **, а не *
users_2 = ["йй", "цц", "уу"]


def say_hi(*user_list, **user_settings):
    for user in user_list:
        for setting in user_settings:
            print(user, setting)


say_hi(*users_2, eyes="green", tall=170)
# всё, что в качестве позиционных аргументов, будет записано в *
# всё, что в качесве именованных аргументов, будет записано в **
