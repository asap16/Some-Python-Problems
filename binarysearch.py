def binarysearch(l, item):
    first = 0
    last = len(l) - 1
    while first <= last:
        mid = (first + last) // 2
        if item < l[mid]:
            last = mid - 1
        elif item > l[mid]:
            first = mid + 1
        else:
            return mid


print(binarysearch([1, 2, 3, 4, 5, 6 ,7], 5))
