# counter = 3
#
# while counter > 0:
#     print("counter", counter)
#     counter -= 1
# else:
#     print("Done")


# a = int(input())
# while a != 0:
#     if a < 0:
#         print('Встретилось отрицательное число', a)
#         break
#     a = int(input())
# else:
#     print('Ни одного отрицательного числа не встретилось')


n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
else:
    print('Ни одного отрицательного числа не встретилось')

