# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

# Пример:

# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5
import random
number = int(input("Введите степень k: "))
result = ""
for i in range (0, number + 1):
    k = random.randint(0, 100)

    if k == 0:
        result = result
    elif i == 0:
        result = str(k)
    elif i == 1:
        result = str(k) + "*x + " + result
    else:
        result = str(k) + "*x^" + str(i) + " + " + result

if result[-1] == " ":
    result = result[:-3]
print(result)
with open("file.txt","w") as f:
    f.write(result)