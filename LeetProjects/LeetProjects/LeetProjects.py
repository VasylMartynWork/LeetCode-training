numbers = [1,2,3]
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        i = 0
        j = 0
        countOfPairs = 0
        while(i < len(nums)):
            j = 0
            while(j < len(nums)):
                if(nums[i] == nums[j] and i < j):
                    countOfPairs += 1
                j += 1
            i += 1
        return countOfPairs

sol = Solution()
print(sol.numIdenticalPairs(numbers))
        