class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second_largest = -1

        for i in range(1, len(nums)):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]

            elif nums[i] < largest and nums[i] > second_largest:
                second_largest = nums[i]

        return second_largest