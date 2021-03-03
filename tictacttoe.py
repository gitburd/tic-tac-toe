import random
from alerts import alerts
from targets import targets

def get_symbol():
    symbols = ["X", "O"]
    symbol = random.choice(symbols)
    return symbol


def play(symbol):
    squares = {'00': ' ', '01': ' ', '02': ' ', '10': ' ', '11': ' ', '12': ' ','20': ' ', '21': ' ', '22': ' '}
    open_squares = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    X_squares = []
    O_squares = []
    alert = ""
    game_over = False
    turn_count = 0
    
    # print(squares['00'])
    # squares = ["00","01","02","10","20","11","21","12","22"]
    print("Let's play TicTacToe! You are", symbol)
    print(display_board(0))
    while turn_count < 5 and game_over == False:
        print(f'{open_squares}')
        turn = input("Make you move!")
        if turn in squares.keys():
            if len(X_squares) >= 2:
                detect_win(X_squares,turn)
            maxRemainingTurns=5
            if symbol == 'X':
                squares[turn]=symbol
                open_squares.remove(turn)
                X_squares.append(turn)
                print_board(squares)
                my_turn(alert,turn,squares, X_squares, O_squares, open_squares)
                turn_count +=1

            else:
                print("I go first!")
        else:
            print("Pick a square!")

def my_turn(alert, turn, squares, X_squares, O_squares, open_squares):
    # first turn

    if len(X_squares) == 1:
        if squares['11'] == " ":
            z = random.choice([1,2])
            if z == 1:
                # take center
                if squares['11'] == " ":
                    squares['11'] = "O"
                    open_squares.remove("11")
                    print_board(squares)
            else:
                # take random
                ran = random.choice(targets[turn])
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
        else:
            # take random
            ran = random.choice(targets[turn])
            squares[ran] = "O"
            open_squares.remove(ran)
            print_board(squares)
    
    elif len(X_squares) == 2:
            # Second turn
        X0 = X_squares[0]
        X1 = X_squares[1]
        # if X1 in targets[X0]:
        # print(f'{X0} {X1}')
        if X0+X1 in alerts:
            if squares[alerts[X0+X1]] == " ":
                squares[alerts[X0+X1]] = "O"
                open_squares.remove(alerts[X0+X1])
                print_board(squares)
            elif squares['11'] == " ":
                squares['11'] = "O"
                open_squares.remove("11")
                print_board(squares)
            else:
                ran = random.choice(open_squares)
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
        else:
            if squares['11'] == " ":
                squares['11'] = "O"
                open_squares.remove("11")
                print_board(squares)
            else:
                ran = random.choice(open_squares)
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
    
    elif len(X_squares) == 3:
        X0 = X_squares[0]
        X1 = X_squares[1]
        X2 = X_squares[2]
        # if X1 in targets[X0]:
        # print(f'{X0} {X1}')
        if X1+X2 in alerts:
            if squares[alerts[X1+X2]] == " ":
                squares[alerts[X1+X2]] = "O"
                open_squares.remove(alerts[X1+X2])
                print_board(squares)
            elif squares['11'] == " ":
                squares['11'] = "O"
                open_squares.remove("11")
                print_board(squares)
            else:
                ran = random.choice(open_squares)
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
        elif X0+X2 in alerts:
            if squares[alerts[X0+X2]] == " ":
                squares[alerts[X0+X2]] = "O"
                open_squares.remove(alerts[X0+X2])
                print_board(squares)
            elif squares['11'] == " ":
                squares['11'] = "O"
                open_squares.remove("11")
                print_board(squares)
            else:
                ran = random.choice(open_squares)
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
        else:
            
            if squares['11'] == " ":
                squares['11'] = "O"
                open_squares.remove("11")
                print_board(squares)
            else:
                ran = random.choice(open_squares)
                squares[ran] = "O"
                open_squares.remove(ran)
                print_board(squares)
    
    elif len(X_squares) == 4:
        X0 = X_squares[0]
        X1 = X_squares[1]
        X2 = X_squares[2]
        X3 = X_squares[3]

        ran = random.choice(open_squares)
        squares[ran] = "O"
        open_squares.remove(ran)
        print_board(squares)
    # alert

def detect_win(squares, turn):
    print(f'in detect win: {squares}, {turn}')
    s0 = squares[0]
    s1 = squares[1]

    # third turn
    if len(squares) == 2:
        if alerts[s0+s1] == turn:
            print(f'detect turn 3 YOU WIN!')
            game_over=True
    # fourth turn
    if len(squares) == 3:
        s2 = squares[2]

        # 00, 01, 02,
        # 11,12
        # 22
        for x in range(0, 3):
            for y in range(x,3):
                if alerts.get(squares[x]+squares[y]) == turn:
                    print(f'detect turn 4 YOU WIN!!!!!')
                    game_over=True
    
    # fifth turn
    if len(squares) == 4:
        s2 = squares[2]
        s3 = squares[3]
        for x in range(0, 4):
            for y in range(x,4):
                if alerts.get(squares[x]+squares[y]) == turn:
                    print(f'detect turn 5 YOU WIN!!!!!')
                    game_over=True


def print_board(squares):
    print(f"""
            {squares['00']}  |  {squares['01']}  |  {squares['02']}
           ---------------
            {squares['10']}  |  {squares['11']}  |  {squares['12']}   
           ---------------
            {squares['20']}  |  {squares['21']}  |  {squares['22']} 
    """)

def display_board(turn):
    board = [
        """
          00  |  01  |  02     
        -------------------
          10  |  11  |  12    
        -------------------
          20  |  21  |  22     
        """
    ]
    if turn == 0:
        return board[0]

def main():
    symbol = get_symbol()
    play("X")
    while input("Play Again? (Y/N) ").upper() == "Y":
        symbol = get_symbol()
        play("X")


if __name__ == "__main__":
    main()