import math
epsilon = 0.00001
def SquareRoot(n):
    
    a = n
    x = n // 2
    y = (x + (a / x)) / 2
    while y != x:
        x = y
        y = (x + (a / x)) / 2
        if abs(y-x) < epsilon:
            break
    return round(y, 2)

print(SquareRoot(2))
