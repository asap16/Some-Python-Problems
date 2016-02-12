def MissingNum(l):
    result = []
    add = 0
    temp = 0
    for i in range(len(l)-1):
        temp = l[i] + 1
        if temp != l[i+1]:
            result.append(l[i] + 1)
            add = l[i] + 2
            while add != l[i+1]:
                result.append(add)
                add += 1

    return result


print(MissingNum([1, 2, 3, 5, 7, 11, 20]))
