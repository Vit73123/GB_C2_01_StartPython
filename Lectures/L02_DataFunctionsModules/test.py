colors = {'red', 'green', 'blue'}       # {} - Задать множество
print(type(colors))                     # type() - Вывести тип данных colors

colors.add('red')
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# colors.remove('red')                    # Ошибка: 'red' уже нет в множестве
colors.discard('red')
print(colors)
colors.discard('gray')
print(colors)
colors.clear()
print(colors)