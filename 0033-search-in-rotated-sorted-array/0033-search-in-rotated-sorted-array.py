class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums)-1

        while left<= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid 
            # left halve is sorted
            if nums[left] <= nums[mid]:
                # if element exists in left halve
                #if taget comes between start and mid 
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1

            else:
                #if element exist in right half
                # if target is betweern mid and end 
                if nums[mid] < target <= nums[right]:
                    left = mid +1

                else:
                    right = mid - 1

        return -1
