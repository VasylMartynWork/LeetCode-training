class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i = 0
        a = len(nums)
        res = []
        while i < a:
            for j in nums:
                if(j % 2 == 0 and i % 2 == 0):
                    res.append(j)
                    nums.remove(j)
                    break
                elif(j % 2 == 1 and i % 2 == 1):
                    res.append(j)
                    nums.remove(j)
                    break
            i += 1
        return res