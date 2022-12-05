from sympy import *

with open('l04th04d_file1', 'r') as f1:
    with open('l04th04d_file2', 'r') as f2:
        with open('l04th04d_file_out', 'w') as fout:
            expr = str(simplify(str(f1.readline() + " + " + f2.readline())))
            fout.write(expr)