"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_number = input("Введите целое число >>> ")

if not user_number.isdigit():
    print("Вы ввели неверный формат числа. Перезапустите программу и попробуйте снова.")
    exit()

# Ver-1
summa = int(user_number) + int(user_number*2) + int(user_number*3)
print(f"{user_number}+{user_number*2}+{user_number*3} = {summa} ")

# Ver-2
# total = 0
# for x in range(1, 4):  # для Х в диапаоне от 1 до 4 не включительно
#     total += int(user_number * x)
#     print(total)
