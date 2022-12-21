# List Comprehension применяется для
# быстрого создания списков

# List Comprehension

# [exp for item in iterable]
# [exp for item in iterable (if condition)]
# [exp <if condition> for item in iterable (if condition)]

# Создать список из чётных чисел

list = []
for i in range(1, 21):     # A - Заполнение списка чётными числами в цикле, с проверкой условия
    if i % 2 == 0:
        list.append(i)
print(list)

list = []                   # B - Заполнение списка всеми числами, без проверки условия
for i in range(1, 21):
    list.append(i)

print(list)

# List Comprehension без if - без проверки условия 

list = []
list = [i for i in range(1, 21)]                # Заполнение списка - идентичен циклу B, без проверки условия
print(list)

# List Comprehension без if - с проверкой условия

list = []
list = [i for i in range(1, 21) if i % 2 == 0]   # Заполнение списка - идентичен циклу A, с проверкой условия
print(list)

# Список кортежей (списка из фиксированных списков - записей)
# [a, b, ... ] - Список
# (a, b, ... ) - Кортеж

# Создать список пар

list = []
list = [(i, i) for i in range(1, 21) if i % 2 == 0]   # Заполнение списка парами чётных чисел
print(list)

# Обработка данных в List Comprehension

def f(x):
    return x ** 2

list = [f(i) for i in range(1, 21) if i % 2 == 0]       # Заполнение списка числами x^2, x - чётные
print(list)

list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]  # Заполнение списка парами (x, x^2), x - чётные
print(list)

