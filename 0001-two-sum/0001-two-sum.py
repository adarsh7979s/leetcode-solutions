class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range (len(nums)):
            needed = target - nums[i]

            if needed not in seen:
                seen[nums[i]] = i

            else:
                return (seen[needed],i)