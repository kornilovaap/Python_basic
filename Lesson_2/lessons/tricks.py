# 1 объединение списков

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = sum(nums, [])
print(total)

# 2 Удаление дубликатов в списке

unique = [1, 2, 3, 3]
unique = list(set(unique))  # преобразовать в список, преобразованный во множество начальный список

# 3 Обмен значениями через кортежи
a = 10
b = 20

a, b = b, a

# 4 Поиск самых часто встречающихся элементов списка

total = [1, 2, 2, 2, 3, 3, 4]
print(
    max(
        set(total),  # set превращает список в множество
        key=total.count  # ключ поиска макс значения
        # при помощи этого ключа находит макс значение во множестве
    )
)

# 5 Распаковка последовательностей при неизвестном количестве элементов
print(total)
print(*total, end=".", sep="-")  # распаковка
 
