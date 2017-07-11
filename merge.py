def mergeSort(ar):
    if len(ar) <= 1:
        return ar

    middle = int(len(ar))

    left = mergeSort(ar[:middle])
    right = mergeSort(ar[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 

    result += left[i:]
    result += right[j:]

    return result