nums = [3,1,2,2,2,1,3]
k = 2

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        i = 0
        co = 0
        while(i < len(nums)):
            j = 0
            while(j < len(nums)):
                if(i < j and nums[i] == nums[j] and (i * j) % k == 0):
                    co += 1
                j += 1
            i += 1
        return co

sol = Solution()
print(sol.countPairs(nums, k))

