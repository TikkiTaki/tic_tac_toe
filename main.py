def print_board(board):
    i=0
    for row in board:
        print(" | ".join(row))
        if i<2:
            print("-" * 9)
            i+=1
        else:
            print(""*9)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)) or \
            all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe(score_X,score_0,draw):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'


    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter the row (1, 2 or 3): \n"))-1
        col = int(input(f"Player {current_player}, enter the column (1, 2 or 3): \n"))-1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                if current_player == "X":
                    score_X += 1
                elif current_player == "O":
                    score_0 += 1

                return(score_X,score_0,draw)
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                draw += 1

                return(score_X,score_0,draw)
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    score_X = 0
    score_0 = 0
    draw = 0
    print("\nWelcome to Tic-Tac-Toe! First player is X, second player is 0\n")
    scoreboard = tic_tac_toe(score_X,score_0,draw)
    print(f"Current scoreboard Player X, Player 0, Draw\n"
          f"                         {scoreboard}")
    play_more = True
    while play_more == True:
        more_games = input("Do you want to play another game? Type Y/N")
        if more_games.upper() == "Y":
            score_X = scoreboard[0]
            score_0 = scoreboard[1]
            draw = scoreboard[2]
            scoreboard = tic_tac_toe(score_X,score_0,draw)
            print(f"Current scoreboard Player X, Player 0, Draw\n"
                  f"                         {scoreboard}")
        else:
            play_more = False
