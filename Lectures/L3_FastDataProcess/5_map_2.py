# map - принимает набор данных и функцию для фильтрации набора данных

ls = [x for x in range(1, 20)]
print(ls)
ls = list(map(lambda x: x + 10, ls))
print(ls)

# map для ввода данных в список

data = list(map(int, input().split()))
print(data)

# Можно не преобразовывать map в list

# В это случае map возвращает не список а указатель н начало итерируемой последовательности (итератор) с её параметрами,
# т.е. при использовании этого объекта указатель проходит по ней и обратно не возвращается,
# поэтому после первого использования объекта map данные в нём очищаются

print("\nmap - итерируемый указатель (итератор(\n")
data = map(int, '1 2 3 4 555 6'.split())        # map без праобразования в список - итерируемый объект
for e in data:
    print(e)

print('--')

for e in data:
    print(e)

# Чтобы данные сохранились в памяти их надо преобразовать из итерируемого объекта в объект с данными
# для этого используется преобразование в список

print("\nСписок\n")
data = list(map(int, '1 2 3 4 555 6'.split()))  # map с преобразованием в list
for e in data:
    print(e)

print('--')

for e in data:
    print(e)

# map ваыполняет ту же работу, что и # пользовательская функция select,
# т.е. вместо select можно использовать map

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)

print("\select\n")
# res = select(lambda x: (x, x ** 2), res)            # lambda функция для построения списка пар (x, x^2), где x - чётные
# print(res)
# аналогично:
res = list(map(lambda x: (x, x ** 2), res))         # map вместо пользовательской функции select

print("\nmap вместо select\n")

print(res)