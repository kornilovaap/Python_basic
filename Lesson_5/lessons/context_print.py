with open('data.txt', 'w') as printable:
    print('Hello', file=printable)
    strings = ["John", "Kate"]

    for x in strings:
        print(x, file=printable)
    
