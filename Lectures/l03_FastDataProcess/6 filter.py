# filter()
# 

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 8 15 23 38'.split()
# data = list(map(int, '1 2 3 4 555 6'.split()))  # map с преобразованием в list

# res = select(int, data)
res = map(int, data)
# res = where(lambda x: not x % 2, res)               # lambda функция для критерия отбора входного списка res в список только с чётными числами
res = filter(lambda x: not x % 2, res)
# res = list(select(lambda x: (x, x ** 2), res))            # lambda функция для построения списка пар (x, x^2), где x - чётные
res = list(map(lambda x: (x, x ** 2), res))            # lambda функция для построения списка пар (x, x^2), где x - чётные
print(res)

