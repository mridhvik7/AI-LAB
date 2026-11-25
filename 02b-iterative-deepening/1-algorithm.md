# Implement Iterative Deepening Search (IDS)

Typed algorithm for this exercise.

1. Set the initial board, goal board, and maximum depth. Use 0 for the blank.
2. Run depth-limited DFS, starting with a depth limit of 0.
3. Return the current path if the state matches the goal. Stop exploring a branch when its remaining depth is 0.
4. Generate legal blank-tile swaps. Skip states already on the current path and backtrack when a branch fails.
5. Increase the depth limit by one and repeat until the search finds a path or reaches the maximum depth.
