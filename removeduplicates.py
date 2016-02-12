'''The program below returns all characters besides the one that are repeated.
It avoids all repetitions. For example, 'noodles' would return 'ndles'. The
order in which strings are concatenated can change due to the use of dictionary.
'''
def RemoveDuplicates(str1):
    d = {}
    result_str = ''
    for i in range(len(str1)):
        d[str1[i]] = d.get(str1[i], 0) + 1
    for k in d:
        if d[k] == 1:
            result_str += str(k)
    return result_str

print(RemoveDuplicates('cutcopypaste'))

'''The program below returns a single item for all repeated items.
For example , [11, 2, 2] would return [11,2].'''
def RemoveDuplicatesList(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(RemoveDuplicatesList([1, 2, 2, 4, 5, 5]))
