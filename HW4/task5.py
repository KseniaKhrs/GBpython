# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from sympy.solvers import solve
from sympy import Symbol
from sympy.simplify import simplify

with open("file1.txt","r") as f1:
    expr1 = f1.read()

with open("file2.txt","r") as f2:
    expr2 = f2.read()
    
x = Symbol('x')
expr3 = simplify(expr1 + " + " + expr2)

with open("file3.txt","w") as f:
    f.write(str(expr3))
