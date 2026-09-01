def findMaxConsecutiveOnes(nums):
    max_ones = 0
    current_ones = 0

    for num in nums:
        if num == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0

    return max_ones


nums1 = [1, 1, 0, 1, 1, 1]
print("Maximum consecutive 1s:", findMaxConsecutiveOnes(nums1))


nums2 = [1, 0, 1, 1, 0, 1]
print("Maximum consecutive 1s:", findMaxConsecutiveOnes(nums2))


nums3 = [0, 0, 0]
print("Maximum consecutive 1s:", findMaxConsecutiveOnes(nums3))


nums4 = [1, 1, 1, 1]
print("Maximum consecutive 1s:", findMaxConsecutiveOnes(nums4))