import random
field = [["-","-","-"], ["-","-","-"], ["-","-","-"]]

print ("ОЧЕРЕДНОСТЬ ИГРОКОВ ОПРЕДЕЛЯЕТСЯ РАНДОМНО\n"+"...\n")
turn = random.randint(0,1)
if turn == 0:
    print("ПЕРВЫМ ХОДИТ ИГРОК")
else:
    print("ПЕРВЫМ ХОДИТ КОМПЬЮТЕР")
gameover = 0
count = 0


while count < 9:

            
    if turn % 2 == 1:
        i = random.randint(0,2)
        j = random.randint(0,2)
        if field [i] [j] == "-":
            field [i] [j] = "O"
            turn += 1
            count += 1
            print("ХОД КОМПЬЮТЕРА")
            print("")
            print('\n'.join(map(' '.join, field)))
            print("")


    else:
        num1 = int(input("Введите номер строки (1,2,3): "))
        num2 = int(input("Введите номер столбца (1,2,3): "))
        if field [num1-1] [num2-1] == "-":
            field [num1-1] [num2-1] = "X"
            turn += 1
            count += 1
            print("ХОД ИГРОКА")
            print("")
            print('\n'.join(map(' '.join, field)))
            print("")

        else:
            print("Указанное поле уже занято")
    if count > 4:
        if (field[0][0] == field[1][1] == field[2][2] == "X" or
            field[0][2] == field[1][1] == field[2][0] == "X" or
            field[0][0] == field[1][0] == field[2][0] == "X" or
            field[0][1] == field[1][1] == field[2][1] == "X" or
            field[0][2] == field[1][2] == field[2][2] == "X" or
            field[0][0] == field[0][1] == field[0][2] == "X" or
            field[1][0] == field[1][1] == field[1][2] == "X" or
            field[2][0] == field[2][1] == field[2][2] == "X") and gameover == 0:
            gameover = 1
            break
        elif (field[0][0] == field[1][1] == field[2][2] == "O" or
            field[0][2] == field[1][1] == field[2][0] == "O" or
            field[0][0] == field[1][0] == field[2][0] == "O" or
            field[0][1] == field[1][1] == field[2][1] == "O" or
            field[0][2] == field[1][2] == field[2][2] == "O" or
            field[0][0] == field[0][1] == field[0][2] == "O" or
            field[1][0] == field[1][1] == field[1][2] == "O" or
            field[2][0] == field[2][1] == field[2][2] == "O") and gameover == 0:
            gameover = 2
            break

if  gameover == 1:
    print("ВЫИГРАЛ ИГРОК")
elif gameover == 2:
    print("ВЫИГРАЛ КОМПЬЮТЕР")
else:
    print("НИЧЬЯ")
