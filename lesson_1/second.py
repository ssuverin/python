# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1]
# and not x[2]) для всех значений предикат.
x = []
for i in range(3):
    x.append(int(input(f'Введите {i + 1}-ое число - ')))

a = not (x[0] or x[1] or x[2])
b = not x[0] and not x[1] and not x[2]
if a == b:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно')
else:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно')
