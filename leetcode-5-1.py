class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = '#'+'#'.join(s)+'#'
        p = [0] * len(s2)
        c = 0
        r = 0
        maxn = 0
        for i in range(1, len(s2)):
            i2 = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[i2])
            else:
                p[i] = 0
            while i+1+p[i] < len(s2) and i-1-p[i] >= 0 and s2[i+1+p[i]] == s2[i-1-p[i]]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
            if p[i] > p[maxn]:
                maxn = i
        return(s2[maxn - p[maxn] + 1: maxn + p[maxn]: 2])

s = "bb"
sol = Solution()
ss = sol.longestPalindrome(s)
print(ss)
