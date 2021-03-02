number = 1


def increment(a):
    print(a)
    a += 1
    print(a)


increment(number)
print(number)

# global

number = 10


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
    start = 0

    def inner_func():
        nonlocal start
        start += 1

    inner_func()
    print(start)


top_func()
