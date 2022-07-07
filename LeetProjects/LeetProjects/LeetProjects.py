nums = [1,2,5,2,3]
target = 2

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if(nums[i] == target):
                res.append(i)

        return res

sol = Solution()
print(sol.targetIndices(nums, target))