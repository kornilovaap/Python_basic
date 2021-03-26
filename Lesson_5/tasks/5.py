"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

# решение со списком случайных чисел
random_list = [randrange(-1000, 1000) for _ in range(15)]

with open("5_random.txt", "w+") as f_random:
    f_random.write(" ".join(map(str, random_list)))

print(f"случайный список: {random_list}\nсумма чисел: {sum(random_list)}")

# решение через ввод чисел пользователем
with open("5_user_input.txt", "w+") as f:
    line = input("Введите числа через пробел >>> ")
    f.writelines(line)
    summa = line.split()

print(f"сумма чисел: {round(sum(map(float, summa)), 2)}")
