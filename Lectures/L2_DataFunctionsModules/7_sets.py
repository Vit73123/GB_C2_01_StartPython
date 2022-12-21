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

# Операции с множествами
# ----------------------

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13,21}

print(a)
print(b)

c = a.copy()                            # Копирование множеств
                                        # создать множество c на основе множества a
print("Копирование:")
print(c)


u = a.union(b)                          # Объединение множеств
print("Объединение:")
print(u)

i = a.intersection(b)                   # Пересечение множеств
print("Пересечение:")
print(i)

dl = a.difference(b)                    # Вычитание множеств: b - a (a из b)
print("Вычитание правого из левого:")
print(dl)

dr = a.difference(b)                    # Вычитание множеств: a - b (b из a)
print("Вычитание левого из правого:")
print(dr)

# Сложная операция с множествами

q = a \
    .union(b) \
    .difference(a.intersection(b))
print("Сложная операция:")
print(q)

# Незименяемые множества - "Замороженные множества"
# "Заморозить" заданное множество

s = set(frozenset(a))                   # "Заморозить" множество - сделать множество неизменяемым