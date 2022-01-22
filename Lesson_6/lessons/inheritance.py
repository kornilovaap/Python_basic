class Person:
    # переменные инкапсулированы и не могут быт доступны на внешних объектах
    _first_name: str
    _last_name: str

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f"{self._first_name} {self._last_name}"


class User(Person):
    login: str
    password: str

    def __init__(self, first_name: str, last_name: str, login: str):
        super().__init__(first_name, last_name)  # super() - возаращает родительский класс, т.е. Person в данном случае
        self.login = login   # перегруили, или переопредили метод добавлением аргумента. Старый класс как работал, так и работает, новый класс принмает новый аргумент

    def log_in(self):
        print(f"Welcome, {self.fullname()}!")


# полиморфзм
class PrinterInfo:
    def info(self, info_object):
        if isinstance(info_object, User):
            print("It's a User!")
        elif isinstance(info_object, Person):
            print("It's a Person!")
        else:
            print("Unknown class/type")


artur = Person("Artur", "Doe")

john = User("Joe", "Doe", "joe_doe")
john.log_in()  # Welcome, Joe Doe!

printer = PrinterInfo()

printer.info(artur)  # It's a Person!
printer.info(john)  # It's a User!
printer.info("Kate")  # Unknown class/type      
                
