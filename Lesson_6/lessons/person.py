class Human:
    age: int
    f_name: str
    l_name: str
    weight: int

    counter: int = 0

    def __init__(self, f_name, l_name, age, weight=0):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.weight = weight

        Human.counter += 1

    def info(self):
        print(f"I'm {self.f_name}, age: {self.age}, weight: {self.weight}")


john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)

john.info()  # I'm John, age: 30, weight: 0
artur.info()  # I'm Artur, age: 40, weight: 0

print(john.counter, artur.counter)  # 2 2
print(Human.counter)  # 2

# print(john, artur)  # <__main__.Human object at 0x000001476244A1C0> <__main__.Human object at 0x0000014762480D60>
#
# john.age = 30
# john.f_name = "John"
# john.l_name = "Doe"
#
# artur.age = 40
# artur.f_name = "Artur"
# artur.l_name = "Doe"

# print(john.f_name, john.l_name, john.age, john.weight)  # John Doe 30 80
# print(artur.f_name, artur.l_name, artur.age, artur.weight)  # Artur Doe 40 80

# john.info()  # I'm John, age: 30, weight: 80
# artur.info()  # I'm Artur, age: 40, weight: 80
    
