def findUnion(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0
    union = []

    while i < n and j < m:

        if arr1[i] <= arr2[j]:
            value = arr1[i]
            i += 1
        else:
            value = arr2[j]
            j += 1

        if not union or union[-1] != value:
            union.append(value)

    while i < n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]

print("Union:", findUnion(arr1, arr2))


arr1 = [1, 1, 1, 1]
arr2 = [2, 2, 3, 3]

print("Union:", findUnion(arr1, arr2))


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

print("Union:", findUnion(arr1, arr2))