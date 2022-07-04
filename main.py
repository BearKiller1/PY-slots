import random
import os

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

point = 10

lose = 0
win = 0
looper = 3;
fruits  = ['ananas', 'banana', 'cherry', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'pear']
keeper = [[0,0,0],[0,0,0],[0,0,0]]

while lose == 0:
    clearConsole()
    for i in range(looper):
        for j in range(3):
            keeper[i][j] = random.choice(fruits)

    # [ 
    #   ['lemon', 'banana', 'pear'], 
    #   ['banana', 'kiwi', 'cherry'], 
    #   ['banana', 'cherry', 'pear']
    # ]

    # Rows
    if fruits[0][0] == fruits[0][1] == fruits[0][2]:
        point += 20
        win = 1
    elif fruits[0][0] == fruits[0][1] or fruits[0][1] == fruits[0][2]:
        point += 10
        win = 1

    if fruits[1][0] == fruits[1][1] == fruits[1][2]:
        point += 20
        win = 1
    elif fruits[1][0] == fruits[1][1] or fruits[1][1] == fruits[1][2]:
        point += 10
        win = 1

    if fruits[2][0] == fruits[2][1] == fruits[2][2]:
        point += 20
        win = 1
    elif fruits[2][0] == fruits[2][1] or fruits[2][1] == fruits[2][2]:
        point += 10
        win = 1

    # Columns   
    if keeper[0][0] == keeper[1][0] == keeper[2][0]:
        point += 15
        win = 1
    if keeper[0][1] == keeper[1][1] == keeper[2][1]:
        point += 15
        win = 1
    if keeper[0][2] == keeper[1][2] == keeper[2][2]:
        point += 15
        win = 1

    # Diagonals
    if keeper[0][0] == keeper[1][1] == keeper[2][2]:
        point += 50
        win = 1
    if keeper[0][2] == keeper[1][1] == keeper[2][0]:
        point += 50
        win = 1

    #zigzag
    if keeper[0][0] == keeper[1][1] == keeper[0][2]:
        point += 5
        win = 1
    if keeper[1][0] == keeper[0][1] == keeper[1][2]:
        point += 5
        win = 1
    if keeper[2][0] == keeper[1][1] == keeper[2][2]:
        point += 5
        win = 1
    # =================== 



    print(colored(3, 252, 102, keeper[0][0] + '\t' + keeper[0][1] + '\t' + keeper[0][2]))
    print(keeper[1][0] + '\t' + keeper[1][1] + '\t' + keeper[1][2])
    print(keeper[2][0] + '\t' + keeper[2][1] + '\t' + keeper[2][2])

    if win == 1:
        win = 0
        print ("You won!")
    else:
        point -= 1

    if point <= 0:
        lose = 1
        print ("You lost all your points!")
        break

    print("\n" + "Your score is: " + str(point) + "\n")
    input("Press Enter to continue...")

