from audioop import reverse


nums = [4,3,10,9,8]

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse = True)
        while True:
            i = 0
            res = 0
            while i <= len(nums):
                res = sum(nums[0:i])
                if(res > sum(nums[i:len(nums)])):
                    return nums[0:i]
                i += 1
            break