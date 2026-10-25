class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(h) - 1
        leftmax = h[left]
        rightmax = h[right]
        water = 0
        if not h:
            return 0
        
        while left< right:
            if leftmax < rightmax:
                left +=1
                leftmax = max(leftmax, h[left])
                water +=  leftmax-h[left]

            else:
                right -=1
                rightmax = max(rightmax, h[right])
                water += rightmax -h[right] 

        return water
