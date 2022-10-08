# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# 1.прочитать файл1 в строчку '2a+5b-18c'
file1 = open("file1.txt", "r")
str1 = file1.readline()
file1.close()

# 2.прочитать файл2 в строчку '5a-2b+4c'
file2 = open("file2.txt", "r")
str2 = file2.readline()
file2.close()

# 3.получить коэффициенты первого многочлена, сохранить в список 1
#kf1 = [2, 5, -18]
str1 = str1.replace('a', ' ')
str1 = str1.replace('b', ' ')
str1 = str1.replace('c', '')
str1 = str1.replace('+', '')
print(str1)
kf1 = str1.split(' ')
# print(kf1)

# 4. получить коэф второго многочлена, сохранить в список 2
# kf2 = [5, -2, 4]
str2 = str2.replace('a', ' ')
str2 = str2.replace('b', ' ')
str2 = str2.replace('c', '')
str2 = str2.replace('+', '')
kf2 = str2.split(' ')

#5.создать список3 и сохранить в него сумму соответ-х элементов списка 1 и 2
kf3 = [0]*len(kf1)
for i in range(len(kf1)):
    kf3[i] = int(kf1[i]) + int(kf2[i])

# 6. сформировать строчку из переменных и коэфициентов   
with open('file_result.txt', 'w') as data:

    for j in range(len(kf3)):
        if(kf3[j] != 0):
            if(j>0 and kf3[j]>0):
                data.write('+')
            data.write(str(kf3[j]))
            if j == 0:
                data.write('a')
            elif j == 1:
                data.write('b')
            elif j == 2:
                data.write('c')



# Result file: '7a+3b-14c'