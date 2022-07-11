nums = [7,5,6,8,3]

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mi = min(nums)
        ma = max(nums)
        grea = 0
        i = 1

        while(i <= mi):
            if(mi % i == 0 and ma % i == 0):
                grea = i
            i += 1
        return grea

sol = Solution()
print(sol.findGCD(nums))