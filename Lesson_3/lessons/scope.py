number = 0


def increment(a):
    print(a)
    a += 1
    print(a)


increment(number)
print(number)

# global

number = 30


def increment(a):
    global result
    result = a + 1
    print(result)
    print(a)


increment(number)
print(number)
print(result)


# не локальная

def top_func():
    start = 5

    def inner_func():
        nonlocal start
        start += 1

    inner_func()
    print(start)


top_func()
________________________________
0
1
0
31
30
30
31
6
 
