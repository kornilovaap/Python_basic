from itertools import count

for x in count(100, 10):
    if x>200:
        break

    print(x)
print('Done')
__________________________
100
110
120
130
140
150
160
170
180
190
200
Done
    
