numbers = [2, 5, 34, 23, 67, 100]
print(numbers)

numbers.append(111)
print(numbers)

numbers.remove(34)
print(numbers)

numbers.append(5)
print(numbers)
print(numbers.count(5))

numbers.extend([20, 30, 40])
print(numbers)

new_list = [50, 60, 70]
new_list.extend(numbers)
print(new_list)

new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)
