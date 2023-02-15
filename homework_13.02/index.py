# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as rdt

amount = int(input("Введите количество элементов в списке: "))
array = [rdt(-20, 21) for i in range(amount)]


min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

result = []

for i in range(amount):
    if min_value <= array[i] and max_value >= array[i]:
        result.append(i)
print(f'Сформированный список: {array}')
print(f'Индексы в диапазоне минимума и максимума: {str(result).strip("[]")}')

