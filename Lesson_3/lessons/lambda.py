# v.1
named_lambda = lambda name: f"Hello, {name}!"

print(named_lambda("John"))

# v.2
print(
    (lambda name: f"Hello, {name}!")
    ("Jack")
)

print(
    (lambda x: x ** 2)
    (2)
)

print(
    (lambda *args: args)
    (1, 2, 3, 3)
)
________________________________
Hello, John!
Hello, Jack!
4
(1, 2, 3, 3)
 
