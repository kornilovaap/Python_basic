from functools import reduce

user_balance = {'Artur': 100, 'Ann': 600, 'John': 300}


def my_balance_func(total, amount):
    return total + amount


user_total = reduce(my_balance_func, user_balance.values())
# sum(user_balance.values())

print(user_total)
