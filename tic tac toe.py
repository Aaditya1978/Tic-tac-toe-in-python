board = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}


def input_check(first1):
    player1 = input("Enter the name of first person:")
    player2 = input("Enter the name of second person:")
    logo1 = int(input(
        "\nChoose whether who will play first(" + player1 + " or " + player2 + ")\nEnter 1 for '" + player1 + "' and 2 for '" + player2 + "' :"))
    print("")
    if logo1 == 1:
        print(player1 + " Will play with X")
        print(player2 + " will play with O")
        print(player1 + " will play first\n")
        first1 = 1
        return 'X', first1, player1, player2
    elif logo1 == 2:
        print(player1 + " Will play with O")
        print(player2 + " will play with X")
        print(player2 + " will play first\n")
        first1 = 2
        return 'O', first1, player1, player2

    else:
        print("Wrong Input!!")
        print("Enter Again\n")
        return 0, first1, player1, player2


def draw_board(inp2, log3):
    inp2 = str(inp2)
    board.update({inp2: log3})
    print("|| " + board['1'] + " | " + board['2'] + " | " + board['3'] + " || ")
    print("------------")
    print("|| " + board['4'] + " | " + board['5'] + " | " + board['6'] + " || ")
    print("------------")
    print("|| " + board['7'] + " | " + board['8'] + " | " + board['9'] + " || ")


def Player1(log1):
    z = 0
    while z == 0:
        inp1 = input("Enter the place number from 1 to 9 where you want your choice:")
        z = num_checker(inp1)
    print("")
    draw_board(inp1, log1)
    print("")


def Player2(log2):
    z = 0
    while z == 0:
        inp1 = input("Enter the place number from 1 to 9 where you want your choice:")
        z = num_checker(inp1)
    print("")
    draw_board(inp1, log2)
    print("")


def num_checker(inp1):
    inp1 = str(inp1)
    if board[inp1] != '':
        print("WRONG INPUT\nPLACE IS ALREADY TAKEN UP\n")
        return 0
    else:
        return 1


def winner():
    if board['7'] == board['8'] == board['9'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['4'] == board['5'] == board['6'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['1'] == board['2'] == board['3'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['1'] == board['4'] == board['7'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['2'] == board['5'] == board['8'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['3'] == board['6'] == board['9'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['7'] == board['5'] == board['3'] != '':
        print("\nGame Over.\n")
        return 0
    elif board['1'] == board['5'] == board['9'] != '':
        print("\nGame Over.\n")
        return 0


count = 9
first = 0
inp = 0
log = ''
print("Welcome To The Game")
logo, first, player1, player2 = input_check(first)
while logo == 0:
    logo, first, player1, player2 = input_check(first)
print("The game starts")
print("")
draw_board(inp, log)
print("")
if first == 1:
    log1 = 'X'
    log2 = 'O'
    while count != 0:
        print(player1 + "'s Turn = X\n")
        Player1(log1)
        count -= 1
        if count < 5:
            stop = winner()
            if stop == 0:
                print(player1 + " Wins!!!!!")
                break
        if count == 0:
            print("IT'S A TIE!!")
            break
        print(player2 + "'s Turn = O\n")
        Player2(log2)
        count -= 1
        if count < 5:
            stop = winner()
            if stop == 0:
                print(player2 + " Wins!!!!!")
                break
        if count == 0:
            print("IT'S A TIE!!")
            break

if first == 2:
    log1 = 'O'
    log2 = 'X'
    while count != 0:
        print(player2 + "'s Turn = X\n")
        Player2(log2)
        count -= 1
        if count < 5:
            stop = winner()
            if stop == 0:
                print(player2 + " Wins!!!!!")
                break
        if count == 0:
            print("IT'S A TIE!!")
            break
        print(player1 + "'s Turn = O\n")
        Player1(log1)
        count -= 1
        if count < 5:
            stop = winner()
            if stop == 0:
                print(player1 + " Wins!!!!!")
                break
        if count == 0:
            print("IT'S A TIE!!")
            break
