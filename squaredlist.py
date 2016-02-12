def SquaredList(l):
    first = 0
    last = len(l)-1
    new_list = []
    while first <= last:
        if l[first]**2 >= l[last]**2:
            new_list.append(l[first]**2)
            first += 1
        elif l[last] ** 2 > l[first] ** 2:
            new_list.append(l[last]**2)
            last -= 1
        
    
    return new_list[::-1]

print(SquaredList([-3, -2, -1, 0, 1, 2, 3]))
