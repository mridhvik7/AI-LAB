from itertools import product


def implies(left, right):
    return not left or right


def tf(value):
    return "T" if value else "F"


models = []
print("KB = (Q -> P) AND (P -> NOT Q) AND (Q OR R)")
print("P Q R | Q->P  P->~Q  QvR | KB")
print("-" * 33)
for p, q, r in product((False, True), repeat=3):
    clauses = (implies(q, p), implies(p, not q), q or r)
    valid = all(clauses)
    if valid:
        models.append((p, q, r))
    a, b, c = map(tf, clauses)
    print(f"{tf(p)} {tf(q)} {tf(r)} |   {a}      {b}    {c}  | {tf(valid)}")

queries = [
    ("NOT Q", lambda p, q, r: not q),
    ("R", lambda p, q, r: r),
    ("R -> P", lambda p, q, r: implies(r, p)),
    ("Q -> R", lambda p, q, r: implies(q, r)),
]
print()
for label, query in queries:
    counterexample = next((m for m in models if not query(*m)), None)
    print(f"KB entails {label}: {counterexample is None}")
    if counterexample is not None:
        p, q, r = map(tf, counterexample)
        print(f"  Counterexample: P={p}, Q={q}, R={r}")
