#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

import math
# list = input("Введите список вещественных чисел (через пробел): ").split()

list = [1.1, 1.2, 3.3, 5, 10.02]
result_list = []
max_length = 1
for i in list:
    if str(i).find(".") != -1:
        tmp = str(i)[str(i).find(".")+1:]
        if len(tmp) > max_length:
            max_length = len(tmp)
        result_list.append(tmp)

for i in range(0, len(result_list)):
    result_list[i] = str(result_list[i]).ljust(max_length,'0')

    while result_list[i].startswith("0") and len(result_list[i]) > 1:
       result_list[i] = result_list[i][1:]
    result_list[i] = int(result_list[i])

print ('0.{}'.format(str(max(result_list) - min(result_list)).rjust(max_length,'0')))