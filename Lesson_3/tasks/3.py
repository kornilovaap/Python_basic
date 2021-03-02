"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    return sum(args) - min(args)


def my_func_2(a, b, c):
    return max(a + b, b + c, c + a)


# lambda
my_func_lambda = lambda a, b, c: max(a + b, b + c, c + a)


print(my_func(1, 2, -3))
print(my_func_2(-1, 2, 0))
print(my_func_lambda(5, -5, 4))
______________________
3
2
9
 
