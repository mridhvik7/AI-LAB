# Implement Alpha–Beta Pruning

Typed algorithm for this exercise.

1. Start at the maximizing root with alpha set to negative infinity and beta set to positive infinity.
2. At each leaf, return its utility. At an internal node, evaluate children recursively, alternating maximizing and minimizing turns.
3. At a maximizing node, keep the highest child value and update alpha. At a minimizing node, keep the lowest child value and update beta.
4. Skip the remaining children when alpha is greater than or equal to beta.
5. Report the root value, the leaf values evaluated, and the number of leaves skipped.
