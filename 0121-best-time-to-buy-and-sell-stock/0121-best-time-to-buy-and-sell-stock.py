class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxp= 0
        # p = 0

        # for i in range(len(prices)):
        #     p = 0
        #     for j in range(i+1,len(prices)):
        #         p = prices[j]-prices[i]

        #         if maxp < p:
        #             maxp = p

        # if maxp <= 0:
        #     return 0

        # return maxp
        minp = prices[0] 
        maxp = 0
        profit = 0
        for price in prices:
            if price < minp:
                minp = price

            else:
                profit = price - minp
                maxp = max(maxp, profit)

        if maxp <= 0:
            return 0
            
        return maxp