# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 24
# 2 2 2 3

num = int(input("Введите натуральное число: "))
lst = []
i = 2
while i * i <= num:
    while num % i == 0:
        lst.append(i)
        num //= i
    i = i + 1
if num > 1:
    lst.append(num)
print(lst)