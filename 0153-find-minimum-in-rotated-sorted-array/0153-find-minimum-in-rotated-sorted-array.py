class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
    
        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]: #this tells us min must be on right halve
                left = mid + 1
            

            else:
                right = mid

        
        return nums[left]
        
                 
