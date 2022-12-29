# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list1 = input("Введите список чисел (через пробел): ").split()
import math

result_list = list((int(list1[x])*int(list1[-x-1])) for x in range(0, math.ceil(len(list1)/2)))
print (result_list)