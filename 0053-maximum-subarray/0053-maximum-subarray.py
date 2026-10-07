class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        csum = 0
        for i in range (len(nums)):
            csum += nums[i]

            if maxsum < csum:
                maxsum = csum

            if csum < 0:
                csum = 0

        return maxsum