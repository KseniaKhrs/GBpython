# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

list_bool = (False, True)
sum = 0
for i in list_bool:
    for j in list_bool:
        for k in list_bool:
            firstResult = not(i or j or k)
            secondResult = (not i) and (not j) and (not k)
            
            if (firstResult==secondResult):
                print ('при X =', i,', Y =', j,', Z =', k, "равенство выполняется")
            else: 
                print ('при X =', i,', Y =', j,', Z =', k, "равенство не выполняется")
                sum += 1
    print()

            
if (sum == 0):
    print ('--> равенство выполняется для любых комбинаций')
else:
    print ('--> равенство выполняется не для всех комбинаций')