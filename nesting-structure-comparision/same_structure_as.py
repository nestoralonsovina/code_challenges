def same_structure_as(original,other):
    for e1, e2 in zip(original, other):
        if type(e1) == type(e2):
            if not same_structure_as(e1, e2):
                return False
        else:
            return False
    return True

assert same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ) == True
assert same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ) == True

assert same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ) == False
assert same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ) == False

assert same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ) == True

assert same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ) == False
