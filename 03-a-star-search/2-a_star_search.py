from heapq import heappop, heappush

START = (2, 8, 3, 1, 6, 4, 0, 7, 5)
GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)
GOAL_POS = {tile: divmod(i, 3) for i, tile in enumerate(GOAL)}


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


def misplaced(state):
    return sum(tile != 0 and tile != GOAL[i] for i, tile in enumerate(state))


def manhattan(state):
    total = 0
    for index, tile in enumerate(state):
        if tile:
            r, c = divmod(index, 3)
            goal_r, goal_c = GOAL_POS[tile]
            total += abs(r - goal_r) + abs(c - goal_c)
    return total


def astar(start, heuristic):
    queue = [(heuristic(start), 0, start)]
    costs = {start: 0}
    parent = {start: None}
    while queue:
        _, cost, state = heappop(queue)
        if cost != costs[state]:
            continue
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for nxt in neighbors(state):
            new_cost = cost + 1
            if nxt not in costs or new_cost < costs[nxt]:
                costs[nxt] = new_cost
                parent[nxt] = state
                heappush(queue, (new_cost + heuristic(nxt), new_cost, nxt))
    return None


methods = [("Misplaced tiles", misplaced),
           ("Manhattan distance", manhattan)]
choice = input("Heuristic (1=misplaced, 2=Manhattan, 3=both): ")
if choice not in {"1", "2", "3"}:
    print("Invalid choice.")
    raise SystemExit

selected = methods if choice == "3" else [methods[int(choice) - 1]]
for name, heuristic in selected:
    path = astar(START, heuristic)
    print(f"{name}: initial h = {heuristic(START)}")
    if path is None:
        print("No solution.\n")
        continue
    print(f"Moves: {len(path) - 1} (0 is blank)")
    for step, state in enumerate(path):
        print(f"Step {step}: {state[:3]} {state[3:6]} {state[6:]}")
    print("Goal reached.\n")
