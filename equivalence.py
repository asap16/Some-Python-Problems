def equivalence(l1, l2):
    if len(l1) >= len(l2):
        for i in l1:
            if i not in l2:
                return False
        return True

print(equivalence([3, 2, 1, 4], [3, 2, 1]))


def Equivalent(l1, l2):
    d = {}
    for i in l1:
        d[i] = d.get(i, 0)+1

    for i in l2:
        if i in d:
            d[i] -= 1
        else:
            return False

    for i in d.values():
        if i != 0:
            return False

    return True

print(Equivalent([3, 2, 1], [3, 1, 2]))
