class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        for i in range (len(nums)):
            if nums[i] not in s:
                s[nums[i]] = 1

            else:
                s[nums[i]] +=1

            
        sorted_s = sorted(s, key=s.get, reverse=True)
        return sorted_s[0]