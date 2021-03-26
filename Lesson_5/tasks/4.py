"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("4.txt", encoding='utf-8') as f:
    lines = f.readlines()

    new_dict = []

    for line in lines:
        line = line.split(' ', 1)
        new_dict.append(dictionary[line[0]] + '  ' + line[1])
    print(new_dict)
    # ['Один  — 1\n', 'Два  — 2\n', 'Три  — 3\n', 'Четыре  — 4']

with open("4_new.txt", "w", encoding='utf-8') as f2:
    f2.writelines(new_dict)
     
