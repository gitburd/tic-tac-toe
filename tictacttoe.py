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
    while turn_count < 5 and not game_over:
        print(f'{open_squares}')
        turn = input("Make you move!")
        if turn in squares.keys():
            if symbol == 'X':
                squares[turn]=symbol
                open_squares.remove(turn)
                X_squares.append(turn)
                print_board(squares)
                if len(X_squares) > 1:
                    if detect_win(X_squares,turn):
                        print(f'YOU WIN!')
                        break
                game_over = my_turn(alert,turn,squares, X_squares, O_squares, open_squares)
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
                    take_square(squares, open_squares, O_squares, "11")
            else:
                # take target
                target = random.choice(targets[turn])
                take_square(squares, open_squares, O_squares, target)
        else:
            # take random
            ran = random.choice(targets[turn])
            take_square(squares, open_squares, O_squares, ran)
    
    # Second turn
    elif len(X_squares) == 2:
        # Defense
        my_move=detect_alert(X_squares, open_squares)
        if my_move is not None:
            take_square(squares, open_squares, O_squares, my_move)
            return False
        # take center
        elif squares['11'] == " ":
            take_square(squares, open_squares, O_squares, "11")
        # take random
        else:
            ran = random.choice(open_squares)
            take_square(squares, open_squares, O_squares, ran)
        
    # third turn
    elif len(X_squares) == 3:
        # Offense
        my_move=detect_alert(O_squares, open_squares)
        if my_move is not None:
            take_square(squares, open_squares, O_squares, my_move)
            print(f'I WIN!')
            return True
        
        # Defense
        my_move=detect_alert(X_squares, open_squares)
        if my_move is not None:
            take_square(squares, open_squares, O_squares, my_move)
            return False

        # X0 = X_squares[0]
        # X1 = X_squares[1]
        # X2 = X_squares[2]


        # if X1+X2 in alerts:
        #     if squares[alerts[X1+X2]] == " ":
        #         take_square(squares, open_squares, O_squares, alerts[X1+X2])
        #     elif squares['11'] == " ":
        #         take_square(squares, open_squares, O_squares, '11')
        #     else:
        #         ran = random.choice(open_squares)
        #         take_square(squares, open_squares, O_squares, ran)
        # elif X0+X2 in alerts:
        #     if squares[alerts[X0+X2]] == " ":
        #         take_square(squares, open_squares, O_squares, alerts[X0+X2])
        #     elif squares['11'] == " ":
        #         take_square(squares, open_squares, O_squares, "11")
        #     else:
        #         ran = random.choice(open_squares)
        #         take_square(squares, open_squares, O_squares, ran)
        else:
            # take center
            if squares['11'] == " ":
                take_square(squares, open_squares, O_squares, "11")
            # take random
            else:
                ran = random.choice(open_squares)
                take_square(squares, open_squares, O_squares, ran)
    # 4th turn
    elif len(X_squares) == 4:
        my_move=detect_alert(O_squares, open_squares)
        print(f'turn 4 my move:{my_move}')
        if my_move is not None:
            take_square(squares, open_squares, O_squares, my_move)
            print(f'turn 4 I WIN!')
            return True

        ran = random.choice(open_squares)
        take_square(squares, open_squares, O_squares, ran)

    # alert
    return False

def take_square(squares, open_squares, O_squares, turn):
    print(f'in take square')
    squares[turn] = "O"
    open_squares.remove(turn)
    O_squares.append(turn)
    print_board(squares)


def detect_alert(squares, open_squares):
    s0 = squares[0]
    s1 = squares[1]

    # third O turn
    # Second X turn
    if len(squares) == 2:
        print(f'detect turn 3 ALERT')
        if alerts.get(s0+s1) in open_squares:
            return alerts.get(s0+s1)

    # fourth O turn
    # third X turn
    if len(squares) == 3:
        s2 = squares[2]

        # 00, 01, 02,n
        # 11,12
        # 22
        for x in range(0, 3):
            for y in range(x,3):
                if alerts.get(squares[x]+squares[y]) in open_squares:
                    print(f'turn 3 detect alert: {alerts.get(squares[x]+squares[y])}')
                    return alerts.get(squares[x]+squares[y])
    return None


def detect_win(squares, turn):
    s0 = squares[0]
    s1 = squares[1]

    # third turn
    if len(squares) == 2:
        if alerts.get(s0+s1) == turn:
            return True
    # fourth turn
    if len(squares) == 3:
        s2 = squares[2]

        # 00, 01, 02,
        # 11,12
        # 22
        for x in range(0, 3):
            for y in range(x,3):
                if alerts.get(squares[x]+squares[y]) == turn:
                    return True

    # fifth turn
    if len(squares) == 4:
        s2 = squares[2]
        s3 = squares[3]
        for x in range(0, 4):
            for y in range(x,4):
                if alerts.get(squares[x]+squares[y]) == turn:
                    return True
    return False


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