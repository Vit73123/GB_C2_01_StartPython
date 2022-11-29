# Множества

# Задать множество
# {}

colors = {'red', 'green', 'blue'}       # {} - Задать множество
print(type(colors))                     # type() - Вывести тип данных colors

# Добавить элемент множества
# add()

colors.add('red')                       # 'red' - уже есть в множестве
                                        # Ошибки не будет, но и добавления элемента не будет
print(colors)                           # Вывод элементов множества

colors.add('gray')                      # 'gray' - добавится в множество
print(colors)

# Удалить элемент множества

# remove() - с ошибкой, если элемента нет в списке
# discard() - нет ошибки, если элемента нет в списке

colors.remove('red')
print(colors)
# colors.remove('red')                    # Ошибка: 'red' уже нет в множестве
colors.discard('red')                    # 'red' уже нет в множестве. Ошибки нет
print(colors)
colors.discard('gray')
print(colors)

# Очистить множество - удалить все элементы

colors.clear()
print(colors)