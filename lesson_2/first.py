# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# x = float(input('Введите число - '))
# sum = 0
# while (x != 0):
#     sum = sum + x % 10
#     x = x // 10
# print(f'Сумма цифр числа равна {sum}')

number = input('Введите вещественное число - ').replace(',', '')
number_list = list(number)
number_list_num = map(int, number_list)
print(f'Сумма цифр числа {number} равна {sum(number_list_num)}')