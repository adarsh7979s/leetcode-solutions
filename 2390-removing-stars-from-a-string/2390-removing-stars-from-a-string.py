class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        s1 = ""
        for i in stack:
            s1 = s1+i
        return s1