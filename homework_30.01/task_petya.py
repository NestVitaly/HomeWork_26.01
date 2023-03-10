from random import randint as rdt

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

summa = int(input("Введите сумму чисел (x, y): "))
product = int(input("Введите произведение чисел (x, y): "))

first_num = 0
second_num = 0

while first_num == 0:
    disc = summa**2 - 4*product # поиск дискриминанта для дальнейшего поиска первого числа
    first_num = (summa + disc) // 2
    if disc > summa: # для исключения отрицательных значений в первом или втором номерах
        second_num = first_num - summa
    else:
        second_num = summa - first_num
print(f'Загаданные числа - {first_num}, {second_num}')