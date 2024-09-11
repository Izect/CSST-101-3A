#basic propositional logic operations
def and_operation(p, q):
    return p and q

def or_operation(p, q):
    return p or q

def not_operation(p):
    return not p

def implies_operation(p, q):
    return not p or q
p = True
q = False

and_test = and_operation(p, q)
or_test = or_operation(p, q)
not_test = not_operation(p)
implies_test = implies_operation(p, q)

print(f"AND operation: {and_test}")
print(f"OR operation: {or_test}")
print(f"NOT operation: {not_test}")
print(f"IMPLIES operation: {implies_test}")