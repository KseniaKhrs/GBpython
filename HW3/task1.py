# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = input("Введите список чисел (через пробел): ").split()
index = 1
sum = 0
while index < len(list):
    sum += int(list[index])
    index += 2
print(sum)