# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("Введите число: "))
list = [1]
for i in range (2, number + 1):
    list.append(list[-1] * i)
print(list)