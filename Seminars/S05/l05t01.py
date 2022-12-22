# 1) В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i - 1]. Найдите это число.
# Пример:   1 2 3 5 6
# Вывод:    4

with open('l05t01_in', 'r') as f:
    lst = [int(num) for num in str(f.readline()).split()]
print(lst)
for i in range(len(lst) - 1):
    if lst[i] + 1 != lst[i + 1]:
        print(lst[i] + 1)
        break