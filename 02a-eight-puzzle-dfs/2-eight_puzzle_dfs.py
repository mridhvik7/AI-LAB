START = (1, 8, 7, 4, 2, 0, 5, 6, 3)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            nxt = list(state)
            other = r * 3 + c
            nxt[blank], nxt[other] = nxt[other], nxt[blank]
            yield tuple(nxt)


def inversion_count(state):
    tiles = [tile for tile in state if tile]
    return sum(
        a > b for i, a in enumerate(tiles) for b in tiles[i + 1:]
    )


def dfs(start, goal):
    if inversion_count(start) % 2 != inversion_count(goal) % 2:
        return None
    stack = [start]
    parent = {start: None}
    while stack:
        state = stack.pop()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            if nxt not in parent:
                parent[nxt] = state
                stack.append(nxt)
    return None


def show(label, state):
    print(label)
    for i in range(0, 9, 3):
        print(*state[i:i + 3])


show("Notebook start board (0 is the blank)", START)
show("Goal (0 is the blank)", GOAL)
start_count = inversion_count(START)
goal_count = inversion_count(GOAL)
print(f"Inversions: start = {start_count}, goal = {goal_count}")
path = dfs(START, GOAL)
print("DFS found a path." if path else "No solution: inversion parity differs.")
print()

# A separate one-move example demonstrates the successful search.
start = (1, 2, 3, 4, 5, 0, 7, 8, 6)
path = dfs(start, GOAL)
print(f"Solvable example: {len(path) - 1} move(s)")
for i, state in enumerate(path):
    show(f"Step {i}", state)
print("Goal reached.")
