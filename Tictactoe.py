def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0

    print("Welcome to Tic Tac Toe!")
    print("Player X goes first.")

    while True:
        print_board(board)
        print(f"Player {players[current_player_index]}'s turn:")

        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2 separated by space): ").split())
            if board[row][col] != " ":
                print("Cell already taken. Choose a different one.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
            continue

        board[row][col] = players[current_player_index]

        if check_winner(board, players[current_player_index]):
            print_board(board)
            print(f"Player {players[current_player_index]} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player_index = 1 - current_player_index

if __name__ == "__main__":
    main()
