class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maximum = 0
        minimum = 0
        for i in range (len(height)):

            minimum = min(height[left], height[right])
            width = right - left
            area = minimum * width

            maximum = max(maximum, area)

            if height[left] < height[right]:
                left+=1

            else:
                right-=1

        return maximum

        