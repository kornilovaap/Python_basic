user = {"name": "John"}

try:
    print(user["age"])
except KeyError:
    print("Invalid key")


try:
    a = 100/0
except ZeroDivisionError:
    print("Zero")
