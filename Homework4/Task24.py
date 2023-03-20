n = int(input('Введите количествао кустов: '))
my_list = []
for i in range(n):
    (a) = int(input(f'Введите количество ягод на {i+1} кусте: '))
    my_list.append(a)
print(my_list)
max = 0
for i in range(len(my_list)-1):
    sum = my_list[i-1] + my_list[i] + my_list[i+1]
    sum = my_list[i-2] + my_list[i-1] + my_list[i]
    if sum > max: max = sum
print(max)
