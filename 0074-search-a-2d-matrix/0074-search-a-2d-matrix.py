class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # values = []
        # for i in matrix:
        #     for mat in i:
        #         values.append(mat)

        # if target in values:
        #     return True
        # else:
        #     return False

        row = len(matrix)  #3 number of rows 
        col = len(matrix[0]) #4 number of col

        top = 0
        bottom = row - 1 # 0, 1, 2

        while top <= bottom:
            midrow = (top + bottom)//2
            if target > matrix[midrow][-1]:
                top = midrow+1

            elif target < matrix[midrow][0]:
                bottom = midrow -1 

            else: # if the target is within the row and neither of above is true 
                break

        if not top <= bottom:
            return False

        midrow = (top + bottom)//2
        left = 0
        right = col - 1

        while left <= right:
            mid = (left + right)//2
            if target < matrix[midrow][mid]:
                right = mid -1 

            elif target > matrix[midrow][mid]:
                left = mid + 1

            else:
                return True

        return False

        

