known = {0 : 0, 1: 1}

def NthFibonacci(n):
    
    if n in known:
        return known[n]
    
    res = NthFibonacci(n - 1) + NthFibonacci(n - 2)

    known[n] = res
    return res

print(NthFibonacci(8))
