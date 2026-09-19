class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        
        # for i in range (len(nums)):
        #     pro = 1
        #     for j in range (len(nums)):
        #         if j != i:
        #             pro = pro*nums[j]

        #     ans.append(pro)

        # return ans

        # n = len(nums)
        # ans = [1] * n

        # for i in range(1, n):
        #     ans[i] = ans[i-1] * nums[i -1]

        # rightproduct = 1
        # for i in range(n-1, -1, -1):
        #     ans[i] = ans[i] * rightproduct 
        #     rightproduct = rightproduct * nums[i]
            
        # return ans



        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res