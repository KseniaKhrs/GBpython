# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. (Дополнительное)

number = int(input("Введите число: "))
if number == 0:
    result = []
else:
    result = [1, 0, 1]
    for i in range(1, number):
        tmp = result[-2]+result[-1]
        result.append(tmp)
        result.insert(0, result[-1]*((-1)**(i)))
print(result)