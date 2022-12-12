# Напишите программу, которая на вход принимает 5 чисел,
# и выводи максимальное из них.

INDEX = 5
nums = []
for num in range(5):
    nums.append(int(input("Введите число: ")))
print(f'max = {max(nums)}')

