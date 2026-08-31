"""Terminal tic-tac-toe for two players."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    print()
    for i, row in enumerate(rows):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def get_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def get_move(player, board):
    while True:
        choice = input(f"Player {player}, enter your move (1-9): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(choice) - 1
        if board[pos] != " ":
            print("That square is already taken.")
            continue
        return pos


def play_round():
    board = [" "] * 9
    player = "X"
    print_board(board)

    while True:
        pos = get_move(player, board)
        board[pos] = player
        print_board(board)

        winner = get_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return

        if " " not in board:
            print("It's a draw!")
            return

        player = "O" if player == "X" else "X"


def main():
    print("Tic-Tac-Toe! Squares are numbered 1-9, left to right, top to bottom.")
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
