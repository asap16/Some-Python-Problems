def RotateIndex(a_list):
    first = 0
    last = len(a_list) - 1
    while first < last:
        mid = (first + last) // 2
        if a_list[mid] < a_list[last] and a_list[mid] < a_list[first]:
            return mid
        elif a_list[mid] > a_list[last]:
            first = mid + 1
        else:
            last = mid - 1

print(RotateIndex([8, 9, 10, 11, 6, 7]))
