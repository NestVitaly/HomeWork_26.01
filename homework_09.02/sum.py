# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sumNumbers(first_num, second_num: int) -> int:
    if first_num == 0:
        return second_num
    else:
        return sumNumbers(first_num - 1, second_num + 1)

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

result = sumNumbers(first_num, second_num)

print(f'Сумма чисел равна: {result}')