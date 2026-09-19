class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for  num in nums:
        #    if nums.count(num) > len(nums)/2:
        #        return num

        # return 0

        # for i in range (len(nums)):
        #     if nums.count(nums[i]) > len(nums)/2:
        #         return nums[i]

        # return 0


        # s = {}
        # for i in range (len(nums)):
        #     if nums[i] not in s:
        #         s[nums[i]] = 1

        #     else:
        #         s[nums[i]] +=1

            
        # sorted_s = sorted(s, key=s.get, reverse=True)
        # return sorted_s[0]

        andidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate