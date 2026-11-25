# Prove a First-Order Logic Query Using Resolution

Typed algorithm for this exercise.

1. Use the same facts and rules as in the forward-reasoning exercise. Convert the rules to clauses by replacing each implication with a disjunction.
2. Instantiate the universally quantified clauses over the constants Asha and Milo.
3. Add the negated query, ¬PetOwner(Asha), to the set of ground clauses.
4. Resolve clauses containing complementary literals. Add each new resolvent and record the two parent clauses.
5. If resolution derives the empty clause, print the proof and report that the knowledge base entails the query. If no new clauses can be derived, report that the query is not entailed.
