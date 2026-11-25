from itertools import product

CONSTANTS = ("Asha", "Milo")
FACTS = {("Cat", "Milo"), ("Owns", "Asha", "Milo")}
RULES = [
    (("x",), [("Cat", "x")], ("Pet", "x")),
    (("x", "y"), [("Owns", "x", "y"), ("Pet", "y")],
     ("PetOwner", "x")),
]


def ground(atom, assignment):
    return (atom[0], *(assignment.get(arg, arg) for arg in atom[1:]))


def show(atom):
    return atom[0] + "(" + ", ".join(atom[1:]) + ")"


def forward_chain(facts, rules, constants):
    known = set(facts)
    while True:
        changed = False
        for variables, conditions, conclusion in rules:
            for values in product(constants, repeat=len(variables)):
                assignment = dict(zip(variables, values))
                premises = [ground(atom, assignment) for atom in conditions]
                result = ground(conclusion, assignment)
                if result not in known and all(p in known for p in premises):
                    known.add(result)
                    print(f"{' and '.join(map(show, premises))} -> {show(result)}")
                    changed = True
        if not changed:
            return known


print("Initial facts:", ", ".join(map(show, sorted(FACTS))))
print("Rules:")
for _, conditions, conclusion in RULES:
    print(" ", " and ".join(map(show, conditions)), "->", show(conclusion))
print("Derivation:")
known = forward_chain(FACTS, RULES, CONSTANTS)
print("Final facts:", ", ".join(map(show, sorted(known))))
for query in [("PetOwner", "Asha"), ("PetOwner", "Milo")]:
    print(f"KB entails {show(query)}: {query in known}")
