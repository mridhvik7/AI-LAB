WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)
EMPTY = "."


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None


def play(board, index, mark):
    return board[:index] + mark + board[index + 1:]


def minimax(board, turn, depth=0):
    result = winner(board)
    if result == "X":
        return 10 - depth
    if result == "O":
        return depth - 10
    if EMPTY not in board:
        return 0

    next_turn = "O" if turn == "X" else "X"
    scores = (
        minimax(play(board, index, turn), next_turn, depth + 1)
        for index, mark in enumerate(board) if mark == EMPTY
    )
    return max(scores) if turn == "X" else min(scores)


def show(board):
    for start in range(0, 9, 3):
        print(" ".join(board[start:start + 3]))
    print()


print("Tic-Tac-Toe | You: O | Computer: X")
print("Cell numbers: 1 2 3 / 4 5 6 / 7 8 9\n")
board = EMPTY * 9
show(board)
while True:
    try:
        move = int(input("Your move: ")) - 1
    except EOFError:
        raise SystemExit
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue
    if not 0 <= move < 9 or board[move] != EMPTY:
        print("Choose an empty cell.")
        continue
    board = play(board, move, "O")
    if winner(board) or EMPTY not in board:
        show(board)
        break

    choices = [i for i, cell in enumerate(board) if cell == EMPTY]
    move = max(choices, key=lambda i: minimax(play(board, i, "X"), "O"))
    board = play(board, move, "X")
    print(f"Computer plays cell {move + 1}.")
    show(board)
    if winner(board) or EMPTY not in board:
        break

result = winner(board)
print("Computer wins (X)." if result == "X" else
      "You win (O)." if result == "O" else "Draw.")
