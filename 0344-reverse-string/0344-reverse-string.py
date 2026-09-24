class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []
        
        for i in s:
            stack.append(i)

        for i in range (len(s)):
           s[i] = stack.pop()

        return s