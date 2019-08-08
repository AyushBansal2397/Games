global p_1
global p_1c
global rp_1
global a_1
global a_1c
global r_1
global a_2
global a_2c
global r_2
global a_3
global a_3c
global r_3
global a_4
global a_4c
global r_4
global ck_p
global ck_1
global ck_2
global ck_3
global ck_4
global q
global w
global ch1
global ch2
global row
global col
global box
global sub_box
global no
global c


def start():

    print("\n\n \t\t\tSUDOKU\n\n")
    for i in range(1):
        print("\t 1) Practice Game")
        print("\t 2) New Game")
        print("\t 3) Load")
        print("\t 4) Exit")

    ch1 = input()

    if ch1 == 1:
        print_p()
    elif ch1 == 2:
        print_1()
    elif ch1 == 3:
        load()
    elif ch1 == 4:
        exit()
    else:
        print("\n\n\t\t\t WARNING!")
        print("\t Enter number between 1 & 4 both inclusive.\n")
        start()


def win():

    print("\n\n\t YOU WON!")

    a_1 = a_1c
    a_2 = a_2c
    a_3 = a_3c
    a_4 = a_4c
    p_1 = p_1c

    start()


def load():

    print("\n\n \t\t\tSUDOKU\n\n")
    for i in range(1):
        print("\t 1) Easy")
        print("\t 2) Intermediate")
        print("\t 3) Hard")
        print("\t 4) Very Hard")

    ch2 = input('\tEnter your choice : ')
    c = ch2==1 or ch2==2 or ch2==3 or ch2==4

    if c:

        if ch2 == 1:
            print_1()
        elif ch2 == 2:
            print_2()
        elif ch2 == 3:
            print_3()
        elif ch2 == 4:
            print_4()
    else:
        print("\n\n\t\t\t WARNING!")
        print("\t Enter number between 1 & 4 both inclusive.\n")
        load()


def change_p(row1, col1, no2):

    if rp_1[row][col] == no2 and p_1[row][col] == 0:
        ck_p -= 1
    p_1[row1][col1] = no2
    if ck_p != 0:
        print_p()
    else:
        win()


def change_1(row1, col1, no2):

    if r_1[row][col]== no2 and a_1[row][col] == 0:
            ck_1 -= 1
    a_1[row1][col1] = no2
    if ck_1 != 0:
        print_1()
    else:
        win()


def change_2(row1, col1, no2):

    if r_2[row][col] == no2 and a_2[row][col] == 0:
        ck_2 -= 1
    a_2[row1][col1] = no2
    if ck_2 != 0:
        print_2()
    else:
        win()


def change_3(row1, col1, no2):

    if r_3[row][col]== no2 and a_3[row][col] == 0:
        ck_3 -= 1
    a_3[row1][col1] = no2
    if ck_3 != 0:
        print_3()
    else:
        win()


def change_4(row1, col1, no2):

    if r_4[row][col]== no2 and a_4[row][col] == 0:
        ck_4 -= 1
    a_4[row1][col1] = no2
    if ck_4 != 0:
        print_4()
    else:
        win()


def deter_pos( box1, sub_box1, no1 ):

    if box1 == 1:

        if sub_box1 < 4:
            row = 0
            col = sub_box1-1

        elif sub_box1 < 7:
            row = 1
            col = sub_box1-4

        else:
            row = 2
            col = sub_box1-7

    if box1 == 2:

        if sub_box1 < 4:
            row = 0
            col = sub_box1+2

        elif sub_box1 < 7:
            row = 1
            col = sub_box1-1

        else:
            row = 2
            col = sub_box1-4

    if box1 == 3:

        if sub_box1 < 4:
            row = 0
            col = sub_box1+5

        elif sub_box1 < 7:
            row = 1
            col = sub_box1+2

        else:
            row = 2
            col = sub_box1-1

    if box1 == 4:

        if sub_box1 < 4:
            row = 3
            col = sub_box1-1

        elif sub_box1 < 7:
            row = 4
            col = sub_box1-4

        else:
            row = 5
            col = sub_box1-7

    if box1 == 5:

        if sub_box1 < 4:
            row = 3
            col = sub_box1+2

        elif sub_box1 < 7:
            row = 4
            col = sub_box1-1

        else:
            row = 5
            col = sub_box1-4

    if box1 == 6:

        if sub_box1 < 4:
            row = 3
            col = sub_box1+5

        elif sub_box1 < 7:
            row = 4
            col = sub_box1+2

        else:
            row = 5
            col = sub_box1-1

    if box1 == 7:

        if sub_box1 < 4:
            row = 6
            col = sub_box1-1

        elif sub_box1 < 7:
            row = 7
            col = sub_box1-4

        else:
            row = 8
            col = sub_box1-7

    if box1 == 8:

        if sub_box1 < 4:
            row = 6
            col = sub_box1+2

        elif sub_box1 < 7:
            row = 7
            col = sub_box1-1

        else:
            row = 8
            col = sub_box1-4

    if box1 == 9:

        if sub_box1 < 4:
            row = 6
            col = sub_box1+5

        elif sub_box1 < 7:
            row = 7
            col = sub_box1+2

        else:
            row = 8
            col = sub_box1-1

    if ch1 == 1:
        change_p(row, col, no1)
    if ch2 == 1:
        change_1(row, col, no1)
    if ch2 == 2:
        change_2(row, col, no1)
    if ch2 == 3:
        change_3(row, col, no1)
    else:
        change_4(row, col, no1)


def value():

    while True:
        box = input(' Enter box no. where you add no. (1-9) : ')
        if box > 9:
            print("\n\n\t\t\t WARNING!")
            print("\t Enter number between 1 & 9 both inclusive.\n")
        else:
            break

    while True:
        sub_box = input(' Enter sub box no. where you add no. (1-9) : ')
        if sub_box > 9:
            print("\n\n\t\t\t WARNING!")
            print("\t Enter number between 1 & 9 both inclusive.\n")
        else:
            break

    while True:
        no = input(' Enter no. which you want add (1-9) : ')
        if no > 9:
            print("\n\n\t\t\t WARNING!")
            print("\t Enter number between 1 & 9 both inclusive.\n")
        else:
            break

    deter_pos(box, sub_box, no)


def print_1():
    print("\n\n \t\t\tSUDOKU\n\n")
    print("\t    0   1   2   3   4   5   6   7   8")
    for q in range(9):
        print("\t  -------------------------------------\n\t", end='')
        for w in range(9):

            if a_1[q][w] == 0:
                print("|   ", end='')
            else:
                print("| " + str(a_1[q][w]) + " ", end='')

        print("|")

    print("\t  -------------------------------------\n\n\n")

    value()


def print_2():
    print("\n\n \t\t\tSUDOKU\n\n")
    print("\t    0   1   2   3   4   5   6   7   8")
    for q in range(9):
        print("\t  -------------------------------------\n\t", end='')
        for w in range(9):

            if a_2[q][w] == 0:
                print("|   ", end='')
            else:
                print("| " + str(a_2[q][w]) + " ", end='')

        print("|")

    print("\t  -------------------------------------\n\n\n")

    value()


def print_3():
    print("\n\n \t\t\tSUDOKU\n\n")
    print("\t    0   1   2   3   4   5   6   7   8")
    for q in range(9):
        print("\t  -------------------------------------\n\t", end='')
        for w in range(9):

            if a_3[q][w] == 0:
                print("|   ", end='')
            else:
                print("| " + str(a_3[q][w]) + " ", end='')

        print("|")

    print("\t  -------------------------------------\n\n\n")

    value()


def print_4():
    print("\n\n \t\t\tSUDOKU\n\n")
    print("\t    0   1   2   3   4   5   6   7   8")
    for q in range(9):
        print("\t  -------------------------------------\n\t", end='')
        for w in range(9):

            if a_4[q][w] == 0:
                print("|   ", end='')
            else:
                print("| " + str(a_4[q][w]) + " ", end='')

        print("|")

    print("\t  -------------------------------------\n\n\n")

    value()


def print_p():
    print("\n\n \t\t\tSUDOKU\n\n")
    print("\t    0   1   2   3   4   5   6   7   8")
    for q in range(9):
        print("\t  -------------------------------------\n\t", end='')
        for w in range(9):

            if p_1[q][w] == 0:
                print("|   ", end='')
            else:
                print("| " + str(p_1[q][w]) + " ", end='')

        print("|")

    print("\t  -------------------------------------\n\n\n")

    value()


if __name__ == '__main__':

    p_1 = [[4, 0, 5, 0, 0, 0, 8, 6, 7],
           [3, 0, 6, 8, 4, 0, 5, 2, 0],
           [8, 0, 7, 0, 6, 5, 0, 9, 3],
           [1, 0, 2, 0, 9, 6, 0, 5, 8],
           [7, 0, 4, 3, 0, 8, 2, 0, 9],
           [9, 5, 0, 7, 1, 0, 6, 0, 4],
           [5, 4, 3, 0, 7, 0, 9, 0, 6],
           [0, 7, 1, 0, 8, 9, 0, 0, 2],
           [2, 8, 0, 6, 0, 0, 1, 0, 5]]
    p_1c = [[4, 0, 5, 0, 0, 0, 8, 6, 7],
            [3, 0, 6, 8, 4, 0, 5, 2, 0],
            [8, 0, 7, 0, 6, 5, 0, 9, 3],
            [1, 0, 2, 0, 9, 6, 0, 5, 8],
            [7, 0, 4, 3, 0, 8, 2, 0, 9],
            [9, 5, 0, 7, 1, 0, 6, 0, 4],
            [5, 4, 3, 0, 7, 0, 9, 0, 6],
            [0, 7, 1, 0, 8, 9, 0, 0, 2],
            [2, 8, 0, 6, 0, 0, 1, 0, 5]]
    rp_1 = [[4, 1, 5, 9, 2, 3, 8, 6, 7],
            [3, 9, 6, 8, 4, 7, 5, 2, 1],
            [8, 2, 7, 1, 6, 5, 4, 9, 3],
            [1, 3, 2, 4, 9, 6, 7, 5, 8],
            [7, 6, 4, 3, 5, 8, 2, 1, 9],
            [9, 5, 8, 7, 1, 2, 6, 3, 4],
            [5, 4, 3, 2, 7, 1, 9, 8, 6],
            [6, 7, 1, 5, 8, 9, 3, 4, 2],
            [2, 8, 9, 6, 3, 4, 1, 7, 5]]

    a_1 = [[3, 0, 0, 0, 9, 0, 4, 1, 0],
           [4, 6, 0, 0, 0, 8, 5, 7, 0],
           [0, 0, 7, 4, 2, 0, 6, 0, 3],
           [0, 4, 0, 0, 0, 2, 9, 0, 0],
           [2, 9, 6, 7, 0, 3, 0, 5, 8],
           [0, 7, 0, 8, 1, 0, 0, 4, 0],
           [7, 0, 9, 0, 5, 4, 3, 0, 0],
           [0, 0, 5, 0, 8, 1, 0, 2, 4],
           [1, 0, 4, 3, 0, 0, 8, 0, 5]]
    a_1c = [[3, 0, 0, 0, 9, 0, 4, 1, 0],
            [4, 6, 0, 0, 0, 8, 5, 7, 0],
            [0, 0, 7, 4, 2, 0, 6, 0, 3],
            [0, 4, 0, 0, 0, 2, 9, 0, 0],
            [2, 9, 6, 7, 0, 3, 0, 5, 8],
            [0, 7, 0, 8, 1, 0, 0, 4, 0],
            [7, 0, 9, 0, 5, 4, 3, 0, 0],
            [0, 0, 5, 0, 8, 1, 0, 2, 4],
            [1, 0, 4, 3, 0, 0, 8, 0, 5]]
    r_1 = [[3, 5, 8, 6, 9, 7, 4, 1, 2],
           [4, 6, 2, 1, 3, 8, 5, 7, 9],
           [9, 1, 7, 4, 2, 5, 6, 8, 3],
           [8, 4, 1, 5, 6, 2, 9, 3, 7],
           [2, 9, 6, 7, 4, 3, 1, 5, 8],
           [5, 7, 3, 8, 1, 9, 2, 4, 6],
           [7, 8, 9, 2, 5, 4, 3, 6, 1],
           [6, 3, 5, 9, 8, 1, 7, 2, 4],
           [1, 2, 4, 3, 7, 6, 8, 9, 5]]

    a_2 = [[0, 0, 8, 2, 4, 1, 0, 0, 3],
           [0, 1, 0, 0, 0, 0, 8, 9, 0],
           [6, 2, 0, 0, 8, 9, 4, 0, 7],
           [7, 6, 9, 1, 0, 0, 0, 0, 5],
           [0, 3, 2, 9, 5, 8, 7, 0, 0],
           [0, 0, 0, 0, 0, 6, 1, 2, 0],
           [0, 9, 7, 0, 0, 2, 0, 4, 0],
           [2, 0, 1, 7, 0, 0, 0, 3, 8],
           [0, 0, 0, 4, 9, 3, 2, 0, 0]]
    a_2c = [[0, 0, 8, 2, 4, 1, 0, 0, 3],
            [0, 1, 0, 0, 0, 0, 8, 9, 0],
            [6, 2, 0, 0, 8, 9, 4, 0, 7],
            [7, 6, 9, 1, 0, 0, 0, 0, 5],
            [0, 3, 2, 9, 5, 8, 7, 0, 0],
            [0, 0, 0, 0, 0, 6, 1, 2, 0],
            [0, 9, 7, 0, 0, 2, 0, 4, 0],
            [2, 0, 1, 7, 0, 0, 0, 3, 8],
            [0, 0, 0, 4, 9, 3, 2, 0, 0]]
    r_2 = [[9, 7, 8, 2, 4, 1, 6, 5, 3],
           [5, 1, 4, 6, 3, 7, 8, 9, 2],
           [6, 2, 3, 5, 8, 9, 4, 1, 7],
           [7, 6, 9, 1, 2, 4, 3, 8, 5],
           [1, 3, 2, 9, 5, 8, 7, 6, 4],
           [4, 8, 5, 3, 7, 6, 1, 2, 9],
           [3, 9, 7, 8, 1, 2, 5, 4, 6],
           [2, 4, 1, 7, 6, 5, 9, 3, 8],
           [8, 5, 6, 4, 9, 3, 2, 7, 1]]

    a_3 = [[9, 0, 2, 0, 0, 0, 0, 6, 8],
           [0, 0, 0, 6, 9, 0, 5, 3, 0],
           [7, 0, 3, 0, 8, 5, 0, 2, 9],
           [2, 0, 6, 0, 0, 8, 0, 9, 3],
           [8, 0, 1, 3, 4, 9, 6, 0, 2],
           [0, 3, 0, 2, 0, 0, 0, 0, 1],
           [3, 2, 0, 0, 5, 0, 9, 0, 6],
           [0, 9, 5, 0, 2, 6, 0, 0, 0],
           [6, 8, 0, 0, 0, 0, 2, 0, 5]]
    a_3c = [[9, 0, 2, 0, 0, 0, 0, 6, 8],
            [0, 0, 0, 6, 9, 0, 5, 3, 0],
            [7, 0, 3, 0, 8, 5, 0, 2, 9],
            [2, 0, 6, 0, 0, 8, 0, 9, 3],
            [8, 0, 1, 3, 4, 9, 6, 0, 2],
            [0, 3, 0, 2, 0, 0, 0, 0, 1],
            [3, 2, 0, 0, 5, 0, 9, 0, 6],
            [0, 9, 5, 0, 2, 6, 0, 0, 0],
            [6, 8, 0, 0, 0, 0, 2, 0, 5]]
    r_3 = [[9, 5, 2, 1, 7, 3, 4, 6, 8],
           [4, 1, 8, 6, 9, 2, 5, 3, 7],
           [7, 6, 3, 4, 8, 5, 1, 2, 9],
           [2, 4, 6, 5, 1, 8, 7, 9, 3],
           [8, 7, 1, 3, 4, 9, 6, 5, 2],
           [5, 3, 9, 2, 6, 7, 8, 4, 1],
           [3, 2, 7, 8, 5, 4, 9, 1, 6],
           [1, 9, 5, 7, 2, 6, 3, 8, 4],
           [6, 8, 4, 9, 3, 1, 2, 7, 5]]

    a_4 = [[0, 0, 9, 7, 0, 0, 0, 3, 8],
           [4, 7, 0, 1, 5, 0, 9, 0, 6],
           [1, 0, 8, 6, 0, 9, 0, 7, 0],
           [0, 0, 2, 5, 7, 0, 8, 0, 1],
           [8, 0, 5, 0, 9, 1, 2, 0, 7],
           [0, 9, 1, 0, 6, 2, 3, 0, 0],
           [0, 5, 0, 2, 0, 6, 0, 1, 3],
           [3, 0, 6, 0, 0, 7, 0, 0, 2],
           [2, 1, 0, 0, 4, 5, 6, 0, 0]]
    a_4c = [[0, 0, 9, 7, 0, 0, 0, 3, 8],
            [4, 7, 0, 1, 5, 0, 9, 0, 6],
            [1, 0, 8, 6, 0, 9, 0, 7, 0],
            [0, 0, 2, 5, 7, 0, 8, 0, 1],
            [8, 0, 5, 0, 9, 1, 2, 0, 7],
            [0, 9, 1, 0, 6, 2, 3, 0, 0],
            [0, 5, 0, 2, 0, 6, 0, 1, 3],
            [3, 0, 6, 0, 0, 7, 0, 0, 2],
            [2, 1, 0, 0, 4, 5, 6, 0, 0]]
    r_4 = [[5, 6, 9, 7, 2, 4, 1, 3, 8],
           [4, 7, 3, 1, 5, 8, 9, 2, 6],
           [1, 2, 8, 6, 2, 9, 5, 7, 4],
           [6, 4, 2, 5, 7, 3, 8, 9, 1],
           [8, 3, 5, 4, 9, 1, 2, 6, 7],
           [7, 9, 1, 8, 6, 2, 3, 4, 5],
           [9, 5, 4, 2, 8, 6, 7, 1, 3],
           [3, 8, 6, 9, 1, 7, 4, 5, 2],
           [2, 1, 7, 3, 4, 5, 6, 8, 9]]

    ck_p = 30
    ck_1 = 38
    ck_2 = 40
    ck_3 = 39
    ck_4 = 36
    q = 0
    w = 0
    ch1 = 0
    ch2 = 0
    row = 0
    col = 0
    box = 0
    sub_box = 0
    no = 0
    c = 1

    start()
