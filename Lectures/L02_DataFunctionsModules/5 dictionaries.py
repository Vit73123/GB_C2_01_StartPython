# Словари

# Получить значение по ключу
# dictionary[ключ]
# Типы ключей могут отличаться

# Задать словарь
# {} - пустой словарь
# {...} - заполнить словарь

# \ - перенос кода на следующую строку (разделить однострочный код на строки)

dictionary = {}                 # Создать пустой словарь
dictionary = \
    {
        'up': ':',              # Заполнить словарь
        'left': '<-',
        'down': '|',
        'right': '->'
    }

print(dictionary)               # Получить весь словарь
print(dictionary['left'])       # Получить значение по ключу

# Получить только ключи
# dictionary.keys()

for k in dictionary.keys():     # keys() - получить ключи
    print(k)

# Получить только значения
# dictionary.keys()

for k in dictionary.values():     # values() - получить значения
    print(k)

# Получить все данные словаря
# dictionary
# dictionary[]
    
for d in dictionary:              # Получить ключи
    print(d)

for v in dictionary:              # Получить значения
    print(dictionary[v])

# Получить пары словаря ключи и значения
    
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))      # Получить пары словаря

# Удалить элемент словаря
# del

del dictionary['left']