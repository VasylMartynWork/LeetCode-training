class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        co = 0
        for i in nums:
            if(len(str(i)) % 2 == 0):
                co += 1
        return co