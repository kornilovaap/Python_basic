def user_generator():
    for user in ("Kate", "John", "Anna"):
        yield user


for user_item in user_generator():
    print(user_item)