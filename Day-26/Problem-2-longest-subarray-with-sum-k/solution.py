class Solution:
    def longestSubarray(self, nums, k):
        current_sum = 0
        prefix_sums = {0: -1}
        max_len = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum - k in prefix_sums:
                length = i - prefix_sums[current_sum - k]
                max_len = max(max_len, length)

            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = i

        return max_len