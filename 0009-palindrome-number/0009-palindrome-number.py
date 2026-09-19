class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

        # if x < 0 or x % 10 == 0:
        #     return False

        # reversed_num = 0
        # original = x

        # while x > 0:
        #     digit = x%10
        #     reversed_num = reversed_num * 10 + digit
        #     x//=10

        # return original == reversed_num