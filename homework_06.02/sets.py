# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

first_num = int(input('Введите числом количество элементов первого списка: '))
second_num = int(input('Введите числом количество элементов второго списка: '))

first_list = []
second_list = []

while len(first_list) != first_num:  # составляем первый список
    print("Значения для первого множества: ")
    for i in range(first_num):
        first_list.append(int(input(f'{i + 1}) ')))

while len(second_list) != second_num:  # составляем второй список
    print("Значения для второго множества: ")
    for i in range(second_num):
        second_list.append(int(input(f'{i + 1}) ')))

print(f'Первое множество - {str(first_list).strip("[]")} \nВторое множество - {str(second_list).strip("[]")}')

# преобразуем списки в множества
first_set = set(first_list)
second_set = set(second_list)
result = sorted((first_set).intersection(second_set))

print(f'Схожие значения: {str(result).strip("[]")}')