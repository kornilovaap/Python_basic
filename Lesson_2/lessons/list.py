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
_________________________________
[2, 5, 34, 23, 67, 100]
[2, 5, 34, 23, 67, 100, 111]
[2, 5, 23, 67, 100, 111]
[2, 5, 23, 67, 100, 111, 5]
2
[2, 5, 23, 67, 100, 111, 5, 20, 30, 40]
[50, 60, 70, 2, 5, 23, 67, 100, 111, 5, 20, 30, 40]
[2, 5, 5, 20, 23, 30, 40, 50, 60, 67, 70, 100, 111]
[111, 100, 70, 67, 60, 50, 40, 30, 23, 20, 5, 5, 2]
 
