def f(x):
    return x ** 2

print(type(f))

# function - тип данных функции

g = f

print(f(1))
print(g(1))

print(type(f(1)))
print(type(g(1)))

print(f(4))
print(g(4))

# Передача функции в аргумент функции

def calc1(x):
    return x + 10

print(calc1(10))

def calc2(x):
    return (x * 10)

def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc1, 10)

# Передача функции с двумя переменными в аргумент функции

def sum(x, y):
    return x + y

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(mult, 4, 5)
