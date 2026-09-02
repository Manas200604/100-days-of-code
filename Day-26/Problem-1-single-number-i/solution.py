class Solution:
    def singleNumber(self, nums):
        l1 = nums.copy()
        l2 = []
        for i in l1:
            if i in l2:
                l2.remove(i)
            else :
                l2.append(i)
        return(l2[0])