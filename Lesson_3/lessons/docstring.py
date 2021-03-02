def hello(word="World"):
    """
    Возврат строки приветсвия
    :param word: Кого приветствуем
    :return: Строка приветсвия
    """
    return f"Hello, {word}"


print(hello())
print(hello("Home"))
