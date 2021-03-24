  
'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''

import os

with open("text.txt") as file:
    text = file.read()
    for line in text:
        lines += 1
            
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
        
        
print ("Количество строк в файле: ", lines)
print ("Кол-во слов: %d" % len(words))
   
