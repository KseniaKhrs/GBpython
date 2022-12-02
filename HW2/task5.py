# Реализуйте алгоритм перемешивания списка.

list = input("Введите элементы списка (через пробел): ").split()
import random
for index in range(0, len(list)):
    index_random = random.randint(0, len(list)-1)
    list[index], list[index_random] = list[index_random], list[index]
print("Список после перемешивания:", list)