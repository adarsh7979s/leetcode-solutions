class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        cmin = prices[0]
        p = 0
        for i in prices:
            if i < cmin:
                cmin = i
            
            p = i - cmin
            maxp = max(maxp , p)

        if maxp == 0:
            return 0

           
        return maxp

