# создали Класс
class Human:
    # переменные объектов (экземляров класса)
    age: int
    f_name: str
    l_name: str
    weight: int
    _password: str
    __bank_account: str

    counter: int = 0

    # конструктор
    def __init__(self, f_name, l_name, age, weight=0):
        # слева - атрибуты экзепляра, справа - аргументы функции
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.weight = weight
        self._int_password()
        self.__bank_account = "123443211234"

        Human.counter += 1

    # создали метод класса
    def info(self):
        print(f"I'm {self.f_name}, age: {self.age}, weight: {self.weight}")

    def _int_password(self):
        self._password = "65432345654321234"

    def show_bank_account(self):
        print(f"Account: {self.__bank_account[:5]}*****************")


# экземпляры класса
john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)

# вызвали метод
john.info()  # I'm John, age: 30, weight: 0
artur.info()  # I'm Artur, age: 40, weight: 0

print(john.counter)  # 2
print(artur.counter)  # 2
print(Human.counter)  # 2

print(john._Human__bank_account)  # получаем доступ к приватной переменной
print(john.show_bank_account())  # безопасный способ доступа к приватной переменной

# print(john, artur)  # <__main__.Human object at 0x000001476244A1C0> <__main__.Human object at 0x0000014762480D60>

# запиали переменные в объект, который является экземпляром класса
# john.age = 30
# john.f_name = "John"
# john.l_name = "Doe"
#
# artur.age = 40
# artur.f_name = "Artur"
# artur.l_name = "Doe"

# print(john.f_name, john.l_name, john.age, john.weight)  # John Doe 30 80
# print(artur.f_name, artur.l_name, artur.age, artur.weight)  # Artur Doe 40 80
   
