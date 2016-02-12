def Min(l):
    min = 0
    for i in range(len(l)-1):
        if l[i] > min:
            min = l[i]
            i += 1
        else:
            min = l[i]
    return min

print(Min([3,0,2,3,4]))
      
