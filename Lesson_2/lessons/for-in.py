name = ["John", "Jack", "Kate"]  # СПИСОК

# index = 0
# while index < len(name):  # len работает и для СТРОК тоже
#     print(f"Hello, {name[index]}")
#     index += 1

# for user in name:
#     print(f"Hello, {user}")
#
# person = {
#     "name": "John",
#     "age": 10}
#
# for key, value in person.items():  # items берет сразу все значения из "строки"
#     print(f"Key {key} = {value}")

for i in range(3):
    for j in range(5):
        if j > i:
            break
        print(i, j)
