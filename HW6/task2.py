# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input("Введите число: "))
result = list([(1+1/x)**x for x in range(1, number+1)])
print (result)
print("сумма равна", sum(result))