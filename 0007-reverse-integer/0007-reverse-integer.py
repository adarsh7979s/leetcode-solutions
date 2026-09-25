class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        if x<0:

            x = -1* x
            s=str(x)
            new_rev=""
            rev = s[::-1]
            res = -1 * int(rev)
            

        else:
            
            s=str(x)
            new_rev=""
            rev = s[::-1]

            res = int(rev)
        
        if res > 2**31 - 1 or res < -2**31:
            return 0

        return res