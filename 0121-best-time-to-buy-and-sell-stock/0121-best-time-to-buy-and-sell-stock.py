class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxdiff = 0
        # diff= 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff= prices[j]-prices[i]
        #         if diff>maxdiff:
        #             maxdiff=diff

        #         if maxdiff<0:
        #             return 0
        # return maxdiff   




        minprice = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]
            else:
                profit =prices[i] - minprice
                maxprofit = max(maxprofit , profit)


        return maxprofit