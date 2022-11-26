# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3, 4]

import random
import math

numsCount = int(input("Предельное число: "))
indexCount = int(input("Количество индексов: "))
numsList = list(range(-numsCount, numsCount + 1))
indexList = [random.randint(0, numsCount * 2) for i in range(indexCount)]
print("Список элементов:\n", numsList)
print("Список индексов:\n", indexList)
print("Перемножаемые элементы:\n", [numsList[index] for index in indexList])
print(math.prod([numsList[index] for index in indexList]))