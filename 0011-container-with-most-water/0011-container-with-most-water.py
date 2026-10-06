class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(h) - 1
        mini = 0
        maxx = 0
        
        for i in range (len(h)):
            mini = min(h[left], h[right])
            width = right - left
            area = mini * width
            if h[left] < h[right]:
                left +=1
            else:
                right -=1

            maxx = max(maxx, area)

        return maxx