num = [8,1,2,2,3]

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            i = 0
            c = 0
            while(i < len(nums)):
                if(nums[i] < num):
                    c += 1
                i += 1
            res.append(c)
        return res

sol = Solution()
print(sol.smallerNumbersThanCurrent(num))