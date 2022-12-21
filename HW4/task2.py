# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

import math 
def simple_digits(n):
    list_simple = []
    for i in range (2, n+1):
        count = 0
        for j in range (2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            list_simple.append(i)
    return list_simple

number = int(input("Введите число: "))
result_list = []
for i in simple_digits(number):
    if number % i == 0:
        result_list.append(i)
print (result_list)