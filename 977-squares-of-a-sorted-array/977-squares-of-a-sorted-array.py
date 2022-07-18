nums = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i = 0
        res = []
        while(i < len(nums)):
            res.append(nums[i] * nums[i])
            i += 1
        res.sort()
        return res

sol = Solution()
print(sol.sortedSquares(nums))