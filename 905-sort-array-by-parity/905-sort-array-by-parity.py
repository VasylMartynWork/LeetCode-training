nums = [3,1,2,4]

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            if(i % 2 == 0):
                res.append(i)
        for j in nums:
            if(j % 2 == 1):
                res.append(j)
        return res

sol = Solution()
print(sol.sortArrayByParity(nums))