# Prove a First-Order Logic Query Using Forward Reasoning

Typed algorithm for this exercise.

1. Start with the ground facts Cat(Milo) and Owns(Asha, Milo).
2. Use the rules Cat(x) → Pet(x) and Owns(x, y) ∧ Pet(y) → PetOwner(x).
3. Substitute known constants for the variables in each rule. If every premise is a known fact, add the rule's conclusion.
4. Repeat until a pass adds no new facts.
5. Look for PetOwner(Asha) in the resulting facts. Print the derivation and the query result.
