# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

from random import randint


print('Ведите число элементов: ')
N = int(input())
numbers = []
for i in range(N):
    numbers.append(randint(2, N))
print(numbers)

exist = []
repeat = []
repeatIsFound = False
for item in numbers:
    for e in exist:
        if item == e:
            repeat.append(e)
            repeatIsFound = True
            break
    if not repeatIsFound:
        exist.append(item)
    repeatIsFound = False
print(exist, repeat)

result = []
for j in exist:
    found = False
    for k in repeat:
        if j == k:
            found = True
    if not found:
        result.append(j)
print(result)
