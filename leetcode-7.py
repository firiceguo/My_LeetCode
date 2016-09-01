class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return(0)
        while x % 10 == 0:
            x = x // 10
        s = str(x)
        if s[0] == '-':
            rev = '-' + s[:0:-1]
        else:
            rev = s[::-1]
        if abs(int(rev)) > 2147483647:
            return(0)
        return(int(rev))

x = 0
sol = Solution()
y = sol.reverse(x)
print(y)
