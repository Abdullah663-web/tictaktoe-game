# Tic Tac Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Check if someone has won
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Main game loop
current_player = "X"
game_over = False

while not game_over:
    # Display the current board
    display_board()

    # Get player move
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # Check if the move is valid
    if board[move] == " ":
        board[move] = current_player
        # Check if the current player has won
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            game_over = True
        # Check for a tie
        elif " " not in board:
            display_board()
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move. Try again.")
