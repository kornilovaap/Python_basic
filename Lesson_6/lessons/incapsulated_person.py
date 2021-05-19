class Person:
    # переменные инкапсулированы и не могут быт доступны на внешних объектах
    _first_name: str
    _last_name: str

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f"Person: {self._first_name} {self._last_name}"


john = Person("Joe", "Doe")
# print(john._last_name)

print(john.fullname())  # Person: Joe Doe

# суть инкапсуляции - мы внутри метода fullname сокрываем логику генерации first_name и last_name в качестве строки
