#Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
X1 = float(input('Введите координату X1: '))
X2 = float(input('Введите координату Y1: '))
Y1 = float(input('Введите координату X2: '))
Y2 = float(input('Введите координату Y2: '))
distance = ((X1 - Y1) ** 2 + (X2 - Y2) ** 2) ** (1/2)
print ('расстояние между точками равно', round(distance,3))