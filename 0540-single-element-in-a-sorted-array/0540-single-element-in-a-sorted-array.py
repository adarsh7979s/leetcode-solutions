class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """                                                           
        left = 0
        right  = len(nums)-1                                            # directly check notes tab 
                                                                        # dry run

        while left < right:
            mid = (left + right)//2
            if mid % 2 == 1:
                mid -=1

            if  nums[mid] == nums[mid+1]: #the target would be on the right
                left = mid +2

            else:
                right = mid

        return nums[left]
