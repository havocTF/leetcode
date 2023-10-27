class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 != 0:
            return False
        half = s[(len(s) / 2)-1:]
        for i in range(len(s)/2):
            if s[i] != half[i]:
                return False
        return True