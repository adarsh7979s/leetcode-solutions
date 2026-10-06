class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # total = 0 

        # for i in range(len(height)):
        #     lmax= 0
        #     rmax = 0

        #     for j in range(i):
        #         lmax = max(lmax , height[j])

        #     for j in range(i+1, len(height)):
        #         rmax = max(rmax, height[j])

        #     water = min(lmax, rmax) - height[i]

        #     if water > 0:
        #         total +=water
                

        # return total

        if not height:
            return 0

        left = 0 
        right = len(height)-1
        leftmax = height[left] 
        rightmax = height[right]
        water = 0
        while left < right:
            if leftmax < rightmax:
                left +=1
                leftmax = max(leftmax, height[left])
                water += leftmax - height[left]
            else:
                right -=1
                rightmax = max(rightmax, height[right])
                water += rightmax - height[right]

        return water
            