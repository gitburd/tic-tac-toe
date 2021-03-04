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
    game_over = False
    turn_count = 0
    
    print("Let's play TicTacToe!")
    print_help()
    print("You are", symbol)
    while turn_count < 5 and not game_over:
        print(f'The open squares are: {open_squares} \n')
        turn = input("Make you move! ")
        if turn.lower() in ['help', 'h']:
            print_help()
        elif turn in open_squares:
            if symbol == 'X':
                squares[turn]=symbol
                print_board(squares)
                if len(X_squares) > 1:
                    if detect_win(X_squares,turn):
                        print(f'YOU WIN!')
                        break
                X_squares.append(turn)
                open_squares.remove(turn)
                game_over = my_turn(turn, squares, X_squares, O_squares, open_squares)
                turn_count +=1
                if turn_count == 5:
                    print("EVERYONE WINS!")
            else:
                print("I go first!")
        else:
            print_help()

def my_turn(turn, squares, X_squares, O_squares, open_squares):
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
        if my_move is not None:
            take_square(squares, open_squares, O_squares, my_move)
            print(f'I WIN!')
            return True

        ran = random.choice(open_squares)
        take_square(squares, open_squares, O_squares, ran)
    return False

def take_square(squares, open_squares, O_squares, turn):
    squares[turn] = "O"
    open_squares.remove(turn)
    O_squares.append(turn)
    print_board(squares)


def detect_alert(squares, open_squares):
    # edge case
    if len(squares) == 2:
        s0 = squares[0]
        s1 = squares[1]
        if alerts.get(s0+s1) in open_squares:
            return alerts.get(s0+s1)

    if len(squares) > 2:
        # 00, 01, 02,
        # 11,12
        # 22
        for x in range(0, len(squares)):
            for y in range(x,len(squares)):
                if alerts.get(squares[x]+squares[y]) in open_squares:
                    return alerts.get(squares[x]+squares[y])
    return None


def detect_win(squares, turn):
    # edge case
    if len(squares) == 2:
        s0 = squares[0]
        s1 = squares[1]
        if alerts.get(s0+s1) == turn:
            return True

    if len(squares) > 2:
        # 00, 01, 02,
        # 11,12
        # 22
        for x in range(0, len(squares)):
            for y in range(x,len(squares)):
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

def print_help():
    print(f"""
          00  |  01  |  02     
        -------------------
          10  |  11  |  12    
        -------------------
          20  |  21  |  22     
        """
    )
    print("Enter 'help' or 'h' to print this again :) \n")

def main():
    symbol = get_symbol()
    play("X")
    while input("Play Again? (Y/N) ").upper() == "Y":
        symbol = get_symbol()
        play("X")


if __name__ == "__main__":
    main()