nums = [5,3,6,1,12]
original = 3

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            j = 0
            for i in nums:
                if(original == i):
                    j += 1
                    original = original * 2
                    break
            if(j == 0):
                return original

sol = Solution()
print(sol.findFinalValue(nums, original))