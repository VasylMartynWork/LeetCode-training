numbers = [4,2,3,3,1,5]
class Solution:
    def buildarray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        if(min(nums) >= 0 and max(nums) <= len(nums) - 1):
            i = 0
            while(i < len(nums)):
                ans[i] = nums[nums[i]]
                i += 1
            return ans
        else:
            return "Array isn't correct"
sol = Solution()
print(sol.buildarray(numbers))