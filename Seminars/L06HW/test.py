# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# Пример:
# 6782 -> 23
# 0,56 -> 11
num = 12.3
comma = '.,'
print(sum(map(int, [i for i in str(num) if not (i in comma)])))