class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            hours = 0
            k = (left+right) // 2
            for pile in piles:
                hours+= (pile +k - 1) // k

            if hours <= h:
                res = min(res, k)
                right = k-1

            else:
                left = k+1

        return res