# В чайле хранятся числа
# Выбрать чётные и составить список пар (число; квадрат числа)

# Пример:
# 1 2 3 5 8 15 23 38
# Вывод:
# [(2, 4), (8, 64), (38, 1444)]

# Загрузить числа из файла - строки с числами

# path = "Z:\\SharedFoler\\GeekBrains\MyProjects\\К2-1 Знакомство с языком Python\\Lectures\\l03_FastDataProcess\\f_nums_in"
path = "f_nums_in"
f = open(path, 'r')
data = f.read() + ' '
data_parse = data
data_split = data
f.close()

# Вариант 1 - Построить список вручную в цикле

numbers = []

while data_parse != '':                             # Разбор строки в цикле
    space_pos = data_parse.index(' ')
    numbers.append(int(data_parse[:space_pos]))
    data_parse = data_parse[space_pos + 1:]

print(numbers)                                      # Вывод - Все числа

out = []

for e in numbers:                                   # Список из пар (x, x^2) - в цикле
    if not e % 2:
        out.append((e, e ** 2))

print(numbers)                                      # Вывод - пары чисел (x, x^2) - после цикла

# Вариант 2 - Построить список вручную через lambda-функции в параметре

# Фильтрация списков с помощью функции, которая принимает в параметре функцию, фильтрующую список

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data_split = data_split.split()                     # Разбор строки с числами методом split()
print(data_split)

res = select(int, data_split)                       # int() - в параметре передаётся встроенная функция,
                                                    # т.е. венрнуть список с преобразованием входного списка data_split в числа int
res = where(lambda x: not x % 2, res)               # lambda функция для критерия отбора входного списка res в список только с чётными числами
res = select(lambda x: (x, x ** 2), res)            # lambda функция для построения списка пар (x, x^2), где x - чётные

print("\nselect\n")