# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import math
number = int(input("Введите число: "))

result_list = list(map(lambda x: math.factorial(x), range (1, number + 1)))
print (result_list)