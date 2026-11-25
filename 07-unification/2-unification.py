def is_variable(term):
    return isinstance(term, str) and term.startswith("?")


def apply(term, substitutions):
    if is_variable(term) and term in substitutions:
        return apply(substitutions[term], substitutions)
    if isinstance(term, tuple):
        name, *args = term
        return (name, *(apply(arg, substitutions) for arg in args))
    return term


def occurs(variable, term):
    if isinstance(term, tuple):
        return any(occurs(variable, arg) for arg in term[1:])
    return variable == term


def unify(left, right):
    substitutions = {}
    pending = [(left, right)]
    while pending:
        a, b = pending.pop()
        a, b = apply(a, substitutions), apply(b, substitutions)
        if a == b:
            continue
        if is_variable(b) and not is_variable(a):
            a, b = b, a
        if is_variable(a):
            if occurs(a, b):
                return None
            substitutions[a] = b
        elif (isinstance(a, tuple) and isinstance(b, tuple)
              and a[0] == b[0] and len(a) == len(b)):
            pending.extend(reversed(list(zip(a[1:], b[1:]))))
        else:
            return None
    return {var: apply(term, substitutions)
            for var, term in substitutions.items()}


def show(term):
    if isinstance(term, tuple):
        name, *args = term
        return name + "(" + ", ".join(map(show, args)) + ")"
    return term.removeprefix("?")


examples = [
    (("loves", "?x", "John"), ("loves", "Mary", "?y")),
    (("knows", "Alice", "Bob"), ("knows", "Alice", "Bob")),
    (("likes", "?x", "?y"), ("hates", "?x", "?y")),
    (("parent", "John", "?x"), ("parent", "Mary", "?y")),
    (("p", "?x"), ("p", ("f", "?x"))),
]
for a, b in examples:
    print(f"Unify {show(a)} with {show(b)}")
    result = unify(a, b)
    if result is None:
        print("  Failure")
    elif not result:
        print("  NIL (empty substitution)")
    else:
        pairs = [f"{show(k)} = {show(v)}" for k, v in result.items()]
        print("  " + ", ".join(pairs))
