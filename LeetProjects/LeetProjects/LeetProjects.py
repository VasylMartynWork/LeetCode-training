nums = [1,3]
k = 3

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        co = 0
        for i in nums:
            for j in nums:
                if(i < j and abs(i - j) == k):
                    co += 1
        return co

sol = Solution()
print(sol.countKDifference(nums, k))