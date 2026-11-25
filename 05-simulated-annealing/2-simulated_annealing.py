from math import exp
import random

N = 8


def conflicts(board):
    return sum(
        board[a] == board[b] or abs(board[a] - board[b]) == b - a
        for a in range(N) for b in range(a + 1, N)
    )


def anneal(start, rng, temperature, cooling, max_steps):
    board = start[:]
    score = conflicts(board)
    step = 0
    while score and step < max_steps and temperature >= 0.0001:
        step += 1
        col = rng.randrange(N)
        candidate = board[:]
        candidate[col] = (board[col] + rng.randrange(1, N)) % N
        candidate_score = conflicts(candidate)
        delta = candidate_score - score
        if delta <= 0 or rng.random() < exp(-delta / temperature):
            board, score = candidate, candidate_score
        temperature *= cooling

    return (board, step) if score == 0 else (None, step)


rng = random.Random(42)
initial = [rng.randrange(N) for _ in range(N)]
print("Initial rows by column:", initial)
print("Initial attacking pairs:", conflicts(initial))
temperature, cooling = 8.0, 0.997
print(f"Initial temperature: {temperature}, cooling rate: {cooling}")
board, steps = anneal(initial, rng, temperature, cooling, 6000)
if board is None:
    print("Cooling schedule ended before a solution was found.")
    raise SystemExit
print("Proposals tested:", steps)
print("Final rows by column:", board)
print("Final attacking pairs:", conflicts(board))
for row in range(N):
    print(" ".join("Q" if q_row == row else "." for q_row in board))
