import random


def conflicts(board):
    return sum(
        board[a] == board[b] or abs(board[a] - board[b]) == b - a
        for a in range(len(board)) for b in range(a + 1, len(board))
    )


def hill_climb(n, rng, max_restarts=500):
    for restart in range(max_restarts + 1):
        board = [rng.randrange(n) for _ in range(n)]
        score = conflicts(board)
        history = [score]
        while score:
            best_board, best_score = board, score
            for col in range(n):
                for row in range(n):
                    if row == board[col]:
                        continue
                    candidate = board[:]
                    candidate[col] = row
                    candidate_score = conflicts(candidate)
                    if candidate_score < best_score:
                        best_board, best_score = candidate, candidate_score

            if best_score == score:
                break
            board, score = best_board, best_score
            history.append(score)
        if score == 0:
            return board, restart, history
    return None, max_restarts, []


try:
    n = int(input("Number of queens: "))
except ValueError:
    print("Enter an integer.")
    raise SystemExit
if n < 1 or n in (2, 3):
    print("No solution for this input.")
    raise SystemExit
board, restarts, history = hill_climb(n, random.Random(12))
if board is None:
    print("No solution found within the restart limit.")
    raise SystemExit

print(f"Random restarts: {restarts}")
print("Conflicts on the successful run:", " -> ".join(map(str, history)))
print("Rows by column (0-based):", board)
print("Attacking pairs:", conflicts(board))
for row in range(n):
    print(" ".join("Q" if q_row == row else "." for q_row in board))
