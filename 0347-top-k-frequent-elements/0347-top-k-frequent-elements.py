class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen ={}

        for i in range (len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1

            else:
                seen[nums[i]] +=1

        sort = sorted(seen, key= seen.get, reverse = True)

        return sort[:k]