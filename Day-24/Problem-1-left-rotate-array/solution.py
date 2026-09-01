def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotate(arr, d):
    n = len(arr)

    # Handle empty array
    if n == 0:
        return

    # Reduce d if it is greater than n
    d = d % n

    # No rotation needed
    if d == 0:
        return

    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse remaining elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse the entire array
    reverse(arr, 0, n - 1)


# Example 1
arr1 = [1, 2, 3, 4, 5]
d1 = 2

leftRotate(arr1, d1)
print("After left rotation:", arr1)


# Example 2
arr2 = [7, 5, 2, 11, 2, 4, 7]
d2 = 6

leftRotate(arr2, d2)
print("After left rotation:", arr2)