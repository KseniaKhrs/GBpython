# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = input("Введите список чисел (через пробел): ").split()
index_first = 0
index_last = len(list) - 1
result_list = []
while index_first <= index_last:
    result_list.append(int(list[index_first]) * int(list[index_last]))
    index_first += 1
    index_last -= 1
print (result_list)