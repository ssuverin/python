# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число - '))
x = []
while number != 0:
    x.append(number)
    number -= 1
lst = []
for i in range(1, number + 1):
    if i == 1:
        x[i] = 1
        lst.append(x[i])
    else:
        x[i] = x[i] * x[i-1]
        lst.append(x[i])
print(lst)