# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint

print('Введите k: ')
k = int(input())
koef = []
for i in range(k + 1):
    koef.append(randint(0, 101))
print(koef)
with open('polynom.txt', 'w') as data:
    for index in range(len(koef)):
        data.write(str(koef[index])) 
        if (k - index) == 0:
            data.write(' = 0')
        elif (k - index) == 1:
            data.write('*x + ')
        else:
            data.write('*x')
            data.write('^')
            data.write(str(k - index))
            data.write(' + ')
# data.close


    