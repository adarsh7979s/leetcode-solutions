class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bottom = row - 1

        while top <= bottom:
            mid = (top + bottom)//2
            if target < matrix[mid][0]:
                bottom = mid -1

            elif target > matrix[mid][-1]:
                top = mid +1

            else:
                break
        
        if not top <= bottom:
            return False
        
        mid = (top + bottom)//2
        left = 0 
        right = col - 1

        while left<=right:
            mid1 =(left+right)//2
            if target < matrix[mid][mid1]:
                right = mid1 -1

            elif target > matrix[mid][mid1]:
                left = mid1 + 1

            else:
                return True

        return False

