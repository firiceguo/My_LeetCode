class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxn1, p1 = 0, 0
        for i, ch in enumerate(s):
            p = 0
            while i - p > -1 and i + p < len(s) and s[i - p] == s[i + p]:
                p = p + 1
            if p > maxn1:
                maxn1 = p
                p1 = i

        maxn2, p2 = 0, 0
        for i, ch in enumerate(s):
            p = 1
            if len(s) < 2:
                break
            while i - p + 1 > -1 and i + p < len(s) and s[i - p + 1] == s[i + p]:
                p = p + 1
            if p > maxn2:
                maxn2 = p
                p2 = i

        if maxn1 >= maxn2:
            return(s[p1 - maxn1 + 1:p1 + maxn1])
        else:
            return(s[p2 - maxn2 + 2:p2 + maxn2])

s = "bb"
sol = Solution()
ss = sol.longestPalindrome(s)
print(ss)
