"""Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

n = int(input("Введите кол-во элементов: "))
array = [int(input()) for i in range (n)]
count=0
print(array)
x = int(input(f'Введите число  x = '))
for i in range(len(array)):
    if x == array[i]:
        count += 1
print(count)

# n = int(input("Введите кол-во элементов: "))
# array = []
# for i in range(n):
#     array.append(i+1)
# print(array)

# x = int(input('Введите число Х= '))
# if x in array: print()
