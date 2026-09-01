def moveZeroes(nums):
    n = len(nums)
    
    # j points to the position
    # where the next non-zero element goes
    j = 0

    # Move all non-zero elements to the front
    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Fill the remaining positions with zeros
    while j < n:
        nums[j] = 0
        j += 1


nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)

nums2 = [0]
moveZeroes(nums2)
print(nums2)

nums3 = [1, 0, 0, 2, 3]
moveZeroes(nums3)
print(nums3)