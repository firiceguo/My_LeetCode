class Solution(object):
    # O(n) Version

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = []
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return(tmp[target - nums[i]], i)
            else:
                tmp[nums[i]] = i

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
