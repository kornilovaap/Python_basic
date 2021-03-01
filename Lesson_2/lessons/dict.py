old_dict = dict(name="John", age=10)
new_dict = {"name": "John", "age": 10}

print(old_dict.keys())
print(old_dict.values())

print(new_dict["age"])
print(new_dict.get("age"))

# print(new_dict["surname"])  не будет работать изза квадратных скобок
print(new_dict.get("surname"))  # функция в таком случае отрабатывает спокойно, поэтому можно "Отработать" ошибку

if new_dict.get("surname") is None:
    print("No surname")
_____________________________
dict_keys(['name', 'age'])
dict_values(['John', 10])
10
10
None
No surname
 
