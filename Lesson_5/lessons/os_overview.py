import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

current_dir = '.'
files = os.listdir(current_dir)
# print(files)
# ['context_print.py', 'context_reader.py', 'os_overview.py', 'simple_reader.py', 'simple_writer.py']

for x in files:
    # print(os.path.dirname(x))  # относительный путь
    # print(os.path.isdir(x))  # True or False
    # print(os.path.dirname(f"./{x}"))  # абсолютный путь
    # print(os.path.dirname("/etc/hosts"))
    print(os.path.split(x))

print(os.path.split("/etc/hosts"))  # ('/etc', 'hosts')

print(os.path.join("/etc/hosts", 'file/', 'hop/test', '1.txt'))  # /etc/hosts\file/hop/test\1.txt
      
