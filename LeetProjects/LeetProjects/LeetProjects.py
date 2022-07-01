nums = [5,6,2,7,4]

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        res = (nums[len(nums) - 1] * nums[len(nums) - 2]) - (nums[0] * nums[1])
        return res

sol = Solution()
print(sol.maxProductDifference(nums))