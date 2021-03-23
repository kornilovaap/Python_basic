import json

person = {
    "name": "John",
    "age": 40,
    "salaries": [100, 200, 160]
}

with open('person.json', 'w') as file_stream:
    json.dump(person, file_stream)
