import sys
from Geek_les_04 import my_mod

print(sys.argv)
# С ПАРАМЕТРАМИ
# задаются через конфигурацию (файл params в этом репозитории)
try:
    file, user, salary = sys.argv
except ValueError:
    print("Invalid args")
    exit()

my_mod.hello(user)
print(my_mod.calculate(float(salary)))
    
