# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    x = int(input('Введите номер четверти - '))
    if x >= 1 and x <= 4:
        break
if x == 1:
    print("x > 0 and y > 0")
elif x == 2:
    print("x < 0 and y > 0")
elif x == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 and y < 0")