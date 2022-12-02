# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

number = int(input("Введите число: "))
list = []
for i in range(-number, number + 1):
  list.append(i) 
print ("Список:", list) 
result = 1 
with open("file.txt", "r") as text:
    index_list = text.read().split(", ")
    for i in index_list:
        result = result * int(list[int(i)])
print ("Произведение элементов на заданных позициях =", result)