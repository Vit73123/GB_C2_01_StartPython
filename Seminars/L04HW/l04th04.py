# 4) Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.

# Пример:
# - k = 2  => 2 * x ^ 2 + 4 * x + 5
# - k = 3  => 41 * x ^ 3 + 6 * x ^ 2 + 2 * x + 98

import random

k = int(input("Введите степень многочлена: "))
lst = [random.randint(0, 100) for i in range(k + 1)]
s = ''
for i in range(k + 1):
    s = s + str(f"{lst[i]}")
    if i < k - 1:
        s = s + str(f" * x ^ {k - i} + ")
    elif i == k - 1:
        s = s + str(f" * x + ")
with open('l04th04_out', 'w') as data:
    data.write(s)