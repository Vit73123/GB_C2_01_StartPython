# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите число: "))

ls = [0]
prev = 0
last = 1
buf = 0
for n in range(1, num + 1):
    ls.insert(0, -last)
    ls.append(last)
    buf = prev + last
    prev = last
    last = buf
print(ls)