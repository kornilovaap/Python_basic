import sys
from Geek_les_04 import my_mod

print(sys.argv)
# С ПАРАМЕТРАМИ
# задаются через конфигурацию (my_mod.cpython-39.pyc)
try:
    file, user, salary = sys.argv
except ValueError:
    print("Invalid args")
    exit()

my_mod.hello(user)
print(my_mod.calculate(float(salary)))
______________________________________
['C:/Users/Im/PycharmProjects/MyStuff/Geek_les_04/main.py', 'test', '10000']
Hello, test
8700.0
    
