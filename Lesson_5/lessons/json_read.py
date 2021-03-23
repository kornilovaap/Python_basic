import json

with open('person.json') as file_stream:
    person = json.load(file_stream)

    print(person)  # {'name': 'John', 'age': 40, 'salaries': [100, 200, 160]}
    print(sum(person['salaries']))  # 460

print(json.loads('{"name": "John", "age": 40, "salaries": [100, 200, 160]}'))
# {'name': 'John', 'age': 40, 'salaries': [100, 200, 160]}
     
