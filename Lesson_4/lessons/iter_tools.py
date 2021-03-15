from itertools import count

for x in count(100, 10):
    if x>200:
        break

    print(x)
print('Done')
