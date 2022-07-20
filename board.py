def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nTry again")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nTry again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nTry again")
                        continue
                except ValueError:
                   print("\nTry again")
                   continue

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1's turn'")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2's turn'")
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
