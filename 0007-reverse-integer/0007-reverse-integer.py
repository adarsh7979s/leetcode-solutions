class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0

        
            
        if x < 0:
            x = -1 * x

            s = str(x)
            s = s[::-1]
            s = "".join(s)
            res = -1* int(s)
            

        else:
            s = str(x)
            s = s[::-1]
            s = "".join(s)
            res = int(s)
            

        if -2**31 <= res <= 2**31 - 1:
            return 0

        return res

