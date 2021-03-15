# генератор списков
import random

tel = '880012345'

tel_list = [f"{tel}{x:02}" for x in range(10) if x not in [4, 5]]

print(tel_list)

# генератор словарей
numbers = [10, 20, 30, 40]

num_dict = {key: key*2 for key in numbers}
print(num_dict)

#
my_set = {el**3 for el in range(1, 5)}
print(sorted(my_set))


random_tel = random.choice(tel_list)
print(random_tel)

# перемешивает список
random.shuffle(tel_list)
print(tel_list)