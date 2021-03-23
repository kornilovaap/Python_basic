with open('data.txt') as my_file:
    print(my_file.read())

print(type(my_file))  # <class '_io.TextIOWrapper'>
# print(my_file.read())  # ValueError: I/O operation on closed file, т.е. файл уже закрылся


# Exception handler
try:
    with open('data.txt') as my_file:
        print(my_file.read())
except IOError:
    print("Some error")
        
