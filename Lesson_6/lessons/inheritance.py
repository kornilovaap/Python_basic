class Person:
    # переменные инкапсулированы и не могут быт доступны на внешних объектах
    _first_name: str
    _last_name: str

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f"Person: {self._first_name} {self._last_name}"


class User(Person):
    login: str
    password: str

    def login(self):
        print(f"Welcome, {self.fullname()}!")


john = User("Joe", "Doe")
john.login()  # Welcome, Person: Joe Doe!
