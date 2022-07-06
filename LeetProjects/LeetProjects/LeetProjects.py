nums = [1,5,4,5]

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        b = nums[len(nums) - 1]
        return (max(nums) - 1) * (nums[len(nums) - 2] - 1)

sol = Solution()
print(sol.maxProduct(nums))