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
_________________________________
['88001234500', '88001234501', '88001234502', '88001234503', '88001234506', '88001234507', '88001234508', '88001234509']
{10: 20, 20: 40, 30: 60, 40: 80}
[1, 8, 27, 64]
88001234500
['88001234501', '88001234502', '88001234508', '88001234503', '88001234500', '88001234506', '88001234507', '88001234509']
   
