# Дополнительное
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Файл1: 2*x² + 4*x + 5
# Файл2: 41*x^3 + 6*x² + 2*x + 98

# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

from sympy import *

with open('l04th04d_file1', 'r') as f1:
    with open('l04th04d_file2', 'r') as f2:
        with open('l04th04d_file_out', 'w') as fout:
            expr = str(simplify(str(f1.readline() + " + " + f2.readline())))
            fout.write(expr)