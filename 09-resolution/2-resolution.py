from itertools import combinations, product

# Each signed literal is (positive, predicate, argument_1, ...).
CONSTANTS = ("Asha", "Milo")
KB = [
    ((), [(True, "Cat", "Milo")]),
    ((), [(True, "Owns", "Asha", "Milo")]),
    (("x",), [(False, "Cat", "x"), (True, "Pet", "x")]),
    (("x", "y"), [
        (False, "Owns", "x", "y"), (False, "Pet", "y"),
        (True, "PetOwner", "x"),
    ]),
]


def negate(literal):
    return (not literal[0], *literal[1:])


def instantiate(kb, constants):
    for variables, clause in kb:
        for values in product(constants, repeat=len(variables)):
            env = dict(zip(variables, values))
            yield frozenset(
                (positive, predicate, *(env.get(a, a) for a in args))
                for positive, predicate, *args in clause
            )


def resolve(a, b):
    for literal in sorted(a):
        opposite = negate(literal)
        if opposite in b:
            result = (a - {literal}) | (b - {opposite})
            if not any(negate(term) in result for term in result):
                yield result


def refute(clauses):
    known = dict.fromkeys(clauses)
    while frozenset() not in known:
        additions = {}
        for a, b in combinations(known, 2):
            for result in resolve(a, b):
                if result not in known:
                    additions.setdefault(result, (a, b))
        if not additions:
            return None
        known.update(additions)
    return known


def show(clause):
    literals = [
        ("" if positive else "~") + predicate + "(" + ", ".join(args) + ")"
        for positive, predicate, *args in sorted(clause)
    ]
    return " OR ".join(literals) if literals else "EMPTY CLAUSE"


def show_proof(clause, proof, printed):
    if clause in printed or proof[clause] is None:
        return
    a, b = proof[clause]
    show_proof(a, proof, printed)
    show_proof(b, proof, printed)
    print(f"Resolve {show(a)}")
    print(f"   with {show(b)}")
    print(f"     => {show(clause)}")
    printed.add(clause)


query = (True, "PetOwner", "Asha")
negated = frozenset({negate(query)})
print("Knowledge base in clause form:")
for _, clause in KB:
    print(" ", show(clause))
print("Negated query:", show(negated))
print("Resolution steps:")
proof = refute([*instantiate(KB, CONSTANTS), negated])
if proof is not None:
    show_proof(frozenset(), proof, set())
print(f"KB entails {show({query})}: {proof is not None}")
