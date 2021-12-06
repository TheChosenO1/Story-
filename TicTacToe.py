game_continue = True
grid = [" ", " " , " ", " ", " ", " ", " ", " ", " "]
x = []
o = [] 
print("\n ********** WELCOME TO TIC-TAC-TOE GAME **********\n")
turn = 0


def reset():
    game_continue = True
    grid = [" ", " " , " ", " ", " ", " ", " ", " ", " "]
    x = []
    o = [] 
    print("\n ********** WELCOME TO TIC-TAC-TOE GAME **********\n")
    turn = 0


def winner_checker():
    global x
    global o
    global turn
    if turn%2 != 0:
        if 1 in x:
            if 2 in x:
                if 3 in x:
                    print("Player 1 has won!")
                    turn=9
            elif 4 in x:
                if 7 in x:
                    print("Player 1 has won!")
                    turn=9
            elif 5 in x:
                if 9 in x:
                    print("Player 1 has won!")
                    turn=9
        elif 2 in x:
            if 5 in x:
                if 8 in x:
                    print("Player 1 has won!")
                    turn=9
        elif 3 in x:
            if 6 in x:
                if 9 in x:
                    print("Player 1 has won!")
                    turn=9
            elif 5 in x:
                if 7 in x:
                    print("Player 1 has won!")
                    turn=9  
        elif 4 in x:
            if 5 in x:
                if 6 in x:
                    print("Player 1 has won!")
                    turn=9
        elif 7 in x:
            if 8 in x:
                if 9 in x:
                    print("Player 1 has won!")
                    turn=9
    else:
        if 1 in o:
            if 2 in o:
                if 3 in o:
                    print("Player 2 has won!")
                    turn=9
            elif 4 in o:
                if 7 in o:
                    print("Player 2 has won!")
                    turn=9
            elif 5 in o:
                if 9 in o:
                    print("Player 2 has won!")
                    turn=9
        elif 2 in o:
            if 5 in o:
                if 8 in o:
                    print("Player 2 has won!")
                    turn=9
        elif 3 in o:
            if 6 in o:
                if 9 in o:
                    print("Player 2 has won!")
                    turn=9
            elif 5 in o:
                if 7 in o:
                    print("Player 2 has won!")  
                    turn=9
        elif 4 in o:
            if 5 in o:
                if 6 in o:
                    print("Player 2 has won!")
                    turn=9
        elif 7 in o:
            if 8 in o:
                if 9 in o:
                    print("Player 2 has won!")
                    turn=9

def input_brain():
    global turn
    looper = True
    turn +=1
    while looper:
        user_input = int(input("Make your move: \n"))
        if user_input >9 or user_input<0:
            print ("Enter a Valid Input")
            continue
        elif user_input in x or user_input in o:
            print("Box Already Occupied")
            continue
        else:
            if turn%2 != 0:
                grid[user_input-1] = "X"
                x.append(user_input)
            else:
                grid[user_input-1] = "O"
                o.append(user_input)
            looper = False

    
def grid_printer():
    global grid
    count = 0
    for each_element in grid:
        count +=1
        if count%3 != 0:
            if count in [1,4,7]:
                print(" "+each_element + '| ', end="" )
            else:
                print(each_element+ "| ", end="")
        else:
            print(each_element, end="")
            print("\n--|--|--")
    count = 0



while game_continue:
    winner_found = False
    while winner_found == False:
        grid_printer()
        print("")
        while turn<9:
            input_brain()
            grid_printer()
            winner_checker()
        question = input("Do you want to play again? (Y/N)\n").capitalize()
        if question == 'Y':
            reset()
        else:
            winner_found =True
            game_continue = False       
    
