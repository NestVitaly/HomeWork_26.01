# 1. Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

'''
print('Введите трёхзначное число!')
numbers = int(input("Ваше число: "))
summa = 0
if numbers < 99 or numbers > 999:
    print("Нужно было вводить именно трёхзначное число!")
else:
    while numbers > 0:
        x = numbers % 10
        summa = summa + x
        numbers = numbers // 10
print(f"Сумма цифр трёхначного числа = {summa} ")
'''



