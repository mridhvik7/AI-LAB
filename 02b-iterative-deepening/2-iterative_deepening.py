START = (1, 2, 3, 5, 0, 6, 4, 7, 8)
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


def depth_limited(state, goal, remaining, path, on_path):
    if state == goal:
        return path[:]
    if remaining == 0:
        return None
    for nxt in neighbors(state):
        if nxt in on_path:
            continue
        on_path.add(nxt)
        path.append(nxt)
        result = depth_limited(nxt, goal, remaining - 1, path, on_path)
        if result is not None:
            return result
        path.pop()
        on_path.remove(nxt)
    return None


def iterative_deepening(start, goal, max_depth):
    for limit in range(max_depth + 1):
        print(f"Trying depth limit {limit}")
        path = depth_limited(start, goal, limit, [start], {start})
        if path is not None:
            return path
    return None


print("Start board:", START)
print("Goal board: ", GOAL)
path = iterative_deepening(START, GOAL, max_depth=12)
if path is None:
    print("No solution within the selected depth.")
    raise SystemExit
print(f"Shortest solution: {len(path) - 1} moves (0 is blank)")
for step, state in enumerate(path):
    print(f"Step {step}: {state[:3]} {state[3:6]} {state[6:]}")
print("Goal reached.")
