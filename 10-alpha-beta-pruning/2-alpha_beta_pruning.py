from math import inf

TREE = (((3, 5), (6, 9)), ((1, 2), (0, -1)))


def alpha_beta(node, alpha, beta, maximizing, visited):
    if isinstance(node, int):
        visited.append(node)
        return node

    best = -inf if maximizing else inf
    for child in node:
        score = alpha_beta(child, alpha, beta, not maximizing, visited)
        if maximizing:
            best = max(best, score)
            alpha = max(alpha, best)
        else:
            best = min(best, score)
            beta = min(beta, best)
        if alpha >= beta:
            break
    return best


def leaves(node):
    if isinstance(node, int):
        return [node]
    return [leaf for child in node for leaf in leaves(child)]


visited = []
score = alpha_beta(TREE, -inf, inf, True, visited)
print("Game tree:", TREE)
print("Leaf order:", leaves(TREE))
print("Evaluated leaves:", visited)
print("Leaves skipped:", len(leaves(TREE)) - len(visited))
print("Optimal root value:", score)
