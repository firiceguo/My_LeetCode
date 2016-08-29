class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxn = 1
        p1 = 0
        p2 = 0
        length = len(s)
        if length == 0:
            return(0)
        while p1 < length - 1 and p2 < length:
            sub = s[p1: p2 + 1]
            if len(sub) > maxn:
                maxn = len(sub)
            p2 = p2 + 1
            if p2 < length and s[p2] in sub:
                p1 = p1 + sub.index(s[p2]) + 1
        return(maxn)

s = "aba"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
