class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        mini = 0
        maxx = 0
        for i in range(len(height)):
            mini = min(height[left],height[right])
            width=right - left
            area = mini* width

            maxx = max(maxx,area)

            if height[left] < height[right]:
                left +=1

            else:
                right -=1

        return maxx



        