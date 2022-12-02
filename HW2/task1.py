# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input("Введите вещественное число: ")
number_string = str(number).replace('.','').replace(',','')
sum = 0
for i in number_string:
    sum += int(i)
print(sum)