"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

start = int(input("Введите стартовое число >>>  "))
end = int(input("Введите конечное число >>> "))

first_list = [x for x in range(start, end + 1)]

print(f"Первый список: {first_list}")

# итератор А. Решение через count
count_list = []
for i in count(start):
    if i > end:
        break
    else:
        count_list.append(i)
print(f"Список через count: {count_list}")

# итератор В
for idx, el in enumerate(cycle(first_list)):
    print(el, end=' ')
    if idx >= 13:
        print()
        break
