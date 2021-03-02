def calculate(salary):
    try:
        return salary - salary * .13  # оклад минус 13%  налог
    except TypeError:  # обработка ошибки
        return None


salary_1 = 100
print(salary_1, calculate(salary_1))

salary_2 = "Test"
print(salary_2, calculate(salary_2))
______________________
100 87.0
Test None
 
