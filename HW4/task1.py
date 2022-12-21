#Вычислить число Пи c заданной точностью d

import math 
number = float(input("Введите число: "))
print("3.{}".format(str(round((math.pi-3)/number))[0:]))