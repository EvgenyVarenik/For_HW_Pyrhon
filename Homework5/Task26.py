"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""

a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))

def power(x, y):
    res = 1
    if y == 0:
        return res
    else:
        res = x * power(x, y-1)
    return res

print(power(a, b))