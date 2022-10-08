# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


print('Введите число: ')
N = int(input())
numsN = []
div = 2
while div <= N:
    if N % div == 0:
        N = N / div
        numsN.append(div)
        div = 2
    else:
        div += 1
print(numsN)