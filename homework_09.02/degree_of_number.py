# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degreeNum(first_num, second_num):
    if second_num == 0: # делаем базис на ввод нуля
        return 1
    if second_num == 1: # базис на ввод единицы
        return first_num
    return first_num * degreeNum(first_num, second_num - 1)

first_num = int(input('Введите число: '))
second_num = int(input('В какую степень будем его возводить: '))
result = degreeNum(first_num, second_num)

print(f'Результат числа "{first_num}", возведённого в степень "{second_num}", равен "{result}"!')