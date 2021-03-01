"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
start = float(input("Введите результат первго дня >>> "))  # a
finish = float(input("Введите желаемый результат >>> "))  # b
days = 1

while start < finish:
    print(f"{days}-й день: {start:.2f}")
    start += start * 0.1
    days += 1
else:
    print(f"{days}-й день: {start:.2f}")

print(f"Ответ: на {days}-й день спортсмен достигнет результата - не менее {finish} км.")
__________________
Введите результат первго дня >>> 2.3
Введите желаемый результат >>> 5
1-й день: 2.30
2-й день: 2.53
3-й день: 2.78
4-й день: 3.06
5-й день: 3.37
6-й день: 3.70
7-й день: 4.07
8-й день: 4.48
9-й день: 4.93
10-й день: 5.42
Ответ: на 10-й день спортсмен достигнет результата - не менее 5.0 км.
  
