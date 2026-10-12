class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # prefix = strs[0]
        # if not strs:
        #     return ""

        # for i in range(1, len(strs)):
        #     while not strs[i].startswith(prefix):
        #         prefix = prefix[:-1]

        #     if prefix == "":
        #         return ""

        # return prefix


        prefix = strs[0]
        if not strs:
            return ""

        for i in range(1, len(strs)):
            j = 0
            while j < len(prefix) and j < len(strs[i]):
                if prefix[j] != strs[i][j]:
                    break
                j +=1
            
            prefix = prefix[:j]
            if prefix == "":
                return ""

        return prefix