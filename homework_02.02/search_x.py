# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint as rdt

length = int(input("Введите число, которое будет соответствовать размеру списка: "))
search_num = int(input("Введите число, которое будем искать в списке: "))

count_search_num = 0
max_value = 0

arr = []
# создаем список с рандомными числами
for _ in range(1, length + 1):
    arr.append(rdt(1, 101))
print(arr)

# ищем заданное число
try:
    for i in range(len(arr)):
        if arr[i] == search_num:
            count_search_num += 1
    print(f'Число {search_num} встречается {count_search_num} раз(а)')
except:
    print()
# поиск ближайшего числа, если заданное число не найдено

try:
    while count_search_num == 0 and max_value < search_num:
        # воспользовался сортировкой (гугл мне в помощь), чтобы найти число больше search_num
        arr = sorted(arr)
        count = 0
        while search_num > max_value:
            max_value = arr[count]
            count += 1
    print(f'Максимально близкое значение к числу {search_num} - {max_value}')
except:
    print("Вы что-то сломали!")