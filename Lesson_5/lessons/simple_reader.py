my_file = open(r'data.txt')  # raw

# print(my_file.readline())  # hello

# print(my_file.readlines())  # ['hello\n', 'world\n', '!!!']

# for line in my_file.readlines():
#     print(line.replace('\n', ''))  # убирает \n из пердыдущего примера и выводит данные так, как мы записали

# print(my_file.read(1024))

print(my_file.closed)  # булева функция, проверка закрыт файл или нет
print(my_file.mode)
print(my_file.name)

for data in my_file.read(10):
    print(data)

print(my_file.tell())
my_file.seek(0, 0)
print(my_file.tell())

my_file.close()
    
