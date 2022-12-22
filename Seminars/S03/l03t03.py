# 3.	Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.

import time

def get_rand(x, y):
    scope = y - x
    print(time.time())
    result = int(time.time() * 10000) % scope
    return result + x

print(get_rand(80, 100))
print(get_rand(20, 100))
print(get_rand(10, 20))