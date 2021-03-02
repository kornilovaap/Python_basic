users = ["Anna", "Roma", "Nina", "Dina"]


def say_hello(*user_list):
    # * - любой аргумент, кот будет передан как позиционный, будет записан в качестве вот этого списка
    for user in user_list:
        print(user)


say_hello(*users)


users_2 = ["Аня", "Рома", "Оля"]


def say_hi(*user_list, **user_settings):
    for user in user_list:
        for setting in user_settings:
            print(user, setting)


say_hi(*users_2, eyes="green", tall=170)
# всё, что в качестве позиционных аргументов, будет записано в *
# всё, что в качесве именованных аргументов, будет записано в **
__________________________________
Anna
Roma
Nina
Dina
Аня eyes
Аня tall
Рома eyes
Рома tall
Оля eyes
Оля tall
 
