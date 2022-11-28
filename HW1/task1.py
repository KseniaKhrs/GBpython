#Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, является ли этот день выходным.
print('Введите число: ')
number = int(input())
if (number >= 1 and number <=5): 
    print ('будний')
elif (number == 6 or number == 7):
    print ('выходной')
else: print ('error')
