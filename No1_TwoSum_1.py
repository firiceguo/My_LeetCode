class Solution(object):
    # O(n^2) Version
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0, len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return([x, y])

    def readNums(self):
        st = input()
        nums = []
        for s in st:
            try:
                n = int(s)
                nums.append(n)
            except Exception:
                pass
        return(nums)

    def readTarget(self):
        return(int(input()))

if __name__ == '__main__':
    sol = Solution()
    nums = sol.readNums()
    target = sol.readTarget()
    print(sol.twoSum(nums, target))
