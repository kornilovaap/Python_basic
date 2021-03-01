name = ["John", "Jack", "Kate"]  # СПИСОК

index = 0
while index < len(name):  # len работает и для СТРОК тоже
    print(f"Hello, {name[index]}")
    index += 1

for user in name:
    print(f"Hi, {user}")

person = {
    "name": "John",
    "age": 10}

for key, value in person.items():  # items берет сразу все значения из "строки"
    print(f"{key} - {value}")

for i in range(1, 4):
    for j in range(1, 6):
        if j > i:
            break
        print(i, j)
_______________________
Hello, John
Hello, Jack
Hello, Kate
Hi, John
Hi, Jack
Hi, Kate
name - John
age - 10
1 1
2 1
2 2
3 1
3 2
3 3
 
