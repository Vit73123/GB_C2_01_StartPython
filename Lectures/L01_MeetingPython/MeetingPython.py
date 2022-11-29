# типы данных и переменная
# int, float, boolean, str, list, None

# Переменные. Динамическое типизирование. Вывод print(). Форматированный вывод. Интерполяция строк
# Строки в '', ""

value = None            # Значение None, чтобы была создана переменная
print('Введите a')      # print()
a = 123                 # Создание переменной int
print('Введите b')
b = 1.23                # Создание переменной float
print(a)
print(b)
value = 12334
print(value)
print(type(value))      # type(переменная) - возвращает тип данных переменной
s = "Hello, \nworld!"   # escape-символ в строке
print(s)
s = "Hello, world!"
print(a,'-', b, '-', s)                     # Вывод через запятую ','
print('{} - {} - {}'.format(a, b, s))       # Форматированный zывод
                                            # Интерполяция строк в {}
                                            # 'string'.format(... , ...)
print('{1} - {2} - {0}'.format(a, b, s))    # Вывод параметров по их номерам
print(f'{a} - {b} - {s}')                   # Интерполяция строк
                                            # f'{Переменная} ...'

f = True                # Булевы значения
print(f)
f = False
print(f)

# Список вместо массива, любые типы данных внутри одного списка

list = []                                   # Пустой список
print(list)                                 # Вывод списка
list = ['1', '2', '3', 'hello']             # Заполнение списка
print(list)
col = ['1', '2', '3', 'hello', 1, 2, 1, 4, 5, True] # Список с разными типами данных
print(col)

# Ввод-вывод. print(). input()

value = None
print('Введите a')
a = input()                                 # input()
                                            # Принимает только строковые значения
print('Введите b')
b = input()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')
print(a, '+', b, ' = ', a + b)

print('Введите a')
a = int(input())                            # Преобразование ввода в целое число
print('Введите b')
b = int(input())
print(a, '+', b, ' = ', a + b)

print('Введите a')
a = float(input())                          # Преобразование ввода в вещественное число
print('Введите b')
b = float(input())
print(a, '+', b, ' = ', a + b)

# Арифметические операции

a = 123
b = 321
c = a + b                                   # + - Сложение
a = +123                                    # + - Унарный плюс
b = -123                                    # - - Унарный минус
a = 2
b = 8
c = a - b                                   # - - Вычитание
c = a * b                                   # * - Умножение
c = b / a                                   # / - Деление в вещественных числах
print(c)
c = a // b                                  # // - Деление в целых числах
print(c)
a = 3
b = 5
c = a % b                                  # % - Остаток от деления
print(c)
c = a ** b                                 # ** - Возведение в степень

# Нет ограничения размера числа

a = 2
b = 800
c = a ** b
print(c)

# Арифметические операции с вещественными числами возвращают некорректный результат
# Всегда требуют округления
# round()

a = 1.3
b = 3
c = a * b                                   # Некорректный результат
print(c)
c = round(a * b)                            # Округление до целого
print(c)
c = round(a * b, 5)                         # Требуется округление для правильного результата выещственного числа, до 5 знаков
print(c)

a = 1.3123
b = 3
c = round(a * b, 5)                         # round() - Округление до 5 знаков
print(c)
a = 1.31231223
b = 3
c = round(a * b, 5)

# Сокращённые операции присваивания

a = 3
a *= 5                                      # *= - Сокращённое присваивание с умножением

# Логические операции

a = 1 > 4
print(a, '1 > 4')
a = 1 < 4
print(a, '1 < 4')
a = 1 < 4 and 5 > 2
print(a, '1 < 4 and 5 > 2')
a = 1 == 2
print(a, '1 == 2')
a = 1 != 2
print(a, '1 != 2')

# Сравнение строк

a = 'qwe'
b = 'qwe'
print(a == b)                               # True - Строки равны

# Сравнение списков

a = [1, 2]
b = [1, 2]
print(a == b)                               # True - Списки равны

# Тройные, и больше равенства, неравенства

a = 1 < 3 < 5                               # Тройное неравенство
print(a)
a = 1 < 3 < 5 < 10                          # Тройное неравенство
print(a)

func = 1
t = 4
x = 123
print(func < t > x)

# Логические операции

f = 1 > 2 or 4 < 6
print(f)

f = [1, 2, 3, 4]
print(f)
print(2 in f)                               # in - принадлежность множеству значений, в том числе в списке
print(not 2 in f)

# Логические значения имеют числовые эквиваленты:
# true = 1, false = 0

is_odd = f[0] % 2 == 0                      # составное выражение: арифметическая + логическая + присваивание
print(is_odd)

# Управляющие конструкции. Важно: соблаюдать отступы!

# if, if-else

a = int(input('a = '))                       # input('Комментарий')
b = int(input('b = '))
if a > b:                                   # if Условие: - без скобок, двоеточие ':'
    print(a)                                # Отступы в if else обязательны!
else:
    print(b)

#elif

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print("Я так ждала Вас, Марина!")
elif username == 'Ильнар':
    print('Ильнар - том')
else:
    print('Привет, ', username)

# while

original = 23
inverted = 0
while original != 0:                            # while - Важно! Соблюдать отступы
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# while else

# Алгоритм: перевернуть число

original = 23
inverted = 0
while original != 0:                            # while - Важно! Соблюдать отступы
    inverted = inverted * 10 + (original % 10)  # Блок while определяется отступами
    original //= 10
else:                                           # else - с циклом while
    print('Пожалуй')                            # Блок else определяется отступами
    print('хватит')
print(inverted)                     

# for с отдельными значениями

for i in 1, 2, 3, 4, 5:                         # for in - перебор отдельных значений
    print(i**2)

# for со списком list

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**2)                                 # for in - перебор списка

# Сплошной набор чисел от нуля - один параметр, задаётся количество чисел, нумерация с нуля

# range(n) - числа от 0 до n - 1

for i in range(5):                              # range(5) - 5 чисел: 0, 1, 2, 3, 4
    print(i)

# range(start, end) - задаётся начальное и конечное числа: от start до end

for i in range (1, 5):                          # range(1, 5) - 5 чисел: 1, 2, 3, 4, 5
    print(i)

# range(start, end, step) - с шагом, задаётся начальное и конечное числа: от start до end с интервалом

for i in range (1, 10, 2):                      # range(1, 10, 2) - 5 чисел: 1, 3, 5, 7, 9
    print(i)

# for со строкой - перебор симолов строки

for c in 'qwe - rty':                           # for со сторокой - перебор символов: q, w, e,  , 0,  , r, t, y
    print(c)

# Строки. API для строк
# len(''), ''.insight(), ''.islower(), ''.replace()

text = 'съешь ещё этих мягких французских булок'

# text.is
print(len(text))                                # 39
print('ещё' in text)                            # True
print(text.insight())                           # False
print(text.islower())                           # True
print(text.replace('ещё', 'ЕЩЁ'))               #

for c in text:
    print(c)

# Срезы для работы со строками, как с массивами
# Поиск подстроки.

text = 'съешь ещё этих мягких французских булок'

print(text[0])                                  # с
print(text[1])                                  # ъ
# print(text[len(text)])                        # IndexError - ошибка, нумерация от 0 до len - 1
print(text[len(text) - 1])                      # к
print(text[-5])                                 # б - отрицательный номер - отсчитывается с конца строки
                                                # -1 - последний символ в строке
print(text[:])                                  # start:end - символы от start до end - 1
                                                # если не указан номер, то принимается соответствующий крайний символ,
                                                # [:] - то же, что и [0: len - 1], т.е. print(text),
                                                # вывод всей строки, т.к. не указан ни один крайний символ,
                                                # вывод от крайнего левого до (включая) крайнего правого
print(text[0:2])                                # съ
print(text[-2:-1])                              # о
print(text[len(text) - 2:])                     # ок
print(text[2:9])                                # ешь ещё
print(text[6:-18])                              # ещё этих мягких
print(text[0:len(text):6])                      # сеикакл
print(text[::6])                                # сеикакл
text = text[2:9] + text[-5] + text[:2]          # ...

# Способы задать список
# Список - пронмуерованная, изменяемая коллекция объектов произвольных типов

numbers = [1, 2, 3, 4, 5]                       # Задать список

# list() - привести range() к списку. range() - это не список

ran = range(1, 6)                               # Задать range 
                                                # [1, 2, 3, 4, 5]
print(type(ran))                                # range - это не список
numbers = list(ran)                             # list(range) - привести range к списку
print(type(numbers))                            # list - это не range

# Со списками можно работать по индексам элементов

print(numbers)                                  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)                                  # [10, 2, 3, 4, 5]

# len() - длина списка

print(f'len {len(numbers)}')                    # len(list) - длина списка

# for со списком

for i in numbers:
    i *= 2                                      # [20, 4, 6, 8, 10]
                                                # Но: изменяются не значения списка, а переменная, которая принимает каждый элемент списка
                                                # т.е. сама переменная элементом списка не является!
    print(i)                                    # [10, 2, 3, 4, 5]
print(numbers)

# append() - Добавить элемент в конец списка
# remove() - Удалить элемент из списка, по его значению!
# del список[номер] - del - ключевое слово (не функци API!); удалить элемент по его номеру

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)                                    # red, green, blue
print()
for e in colors:
    print(e * 2)                                # redred greengreen blueblue
                                                # * число повторений - со строкой - повторить строку заданной количество раз
print()
colors.append('gray')                           # append()

print(colors == ['red', 'green', 'blue', 'gray'])   # True
for e in colors:
    print(e)                                    # red, green, blue, gray
print()
colors.remove('red')                            # remove(значение элемента) - удалить элемент из списка
for e in colors:
    print(e)                                    # green, blue, gray
print()
del colors[0] 
for e in colors:
    print(e)                                    # blue, gray
print()                                         # del список[индекс] - удалить элемент списка по индексу

# Функции (методы). Соблюдать отступы (пробелы / табуляция) для ограничения тела функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return                                  # Пустой return - возвращает значение None

arg = 2
print(f(arg))
print(type(f(arg)))


# help(Оператор) - вывести справку по оператору
# Оператор записывается в полной рабочей конструкции

help(text.istitle)                              # help() - Вывести в консоли справку по методу istitle

# Заевршить программу
# exit()

exit()