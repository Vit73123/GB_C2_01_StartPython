# Lamda-функция
# Псевдоним функции

def sum_f(x, y):
    return x + y

f = sum_f                 # f - псевдоним sum()

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(f, 4, 5)

f = lambda x, y: x + y  # f - lambda функция

calc(f, 4, 5)

sum = lambda q, w: q + w  # f - lambda функция

calc(sum, 4, 5)

# Передача lambda функции в аргумент функции

calc (lambda q, w: q + w, 4, 5)