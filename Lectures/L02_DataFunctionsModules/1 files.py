# Файлы
# -------------------------------------------------------------------------------------

# Открыть, записать, закрыть файл

# open()
# Надо обязательно закрывать файл - close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors)             # Разделителей не будет
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()                        # Надо обязательно закрыть файл

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)             # Разделителей не будет
data.close()

# with open() as data
# Файл закрывает автоматически по выходу из блока with. Можно вручную закрывать не надо

with open('file.txt', 'w') as data:
    data.write('Line1\n')
    data.write('Line2\n')           # Файл закрывает автоматически по выходу из блока with.

# Чтение файла
# line in data
    
# Все данные считываются как текст
# При считывании числовых данных требуется конвертация!

path = 'file.txt'
data = open(path, 'r')              # open()
for line in data:                   # line in data
    print(line)
data.close()                        # close()
exit()                              # exit()