numbs = [1,2,3,4]
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        i = 0
        numbe = []
        res = []
        while(i < len(nums) / 2):
            pair = nums[2 * i:2 * i + 2]
            numbe.append([pair[1]] * pair[0])
            i += 1
        for n in numbe:
            res += n
        return res

sol = Solution()
print(sol.decompressRLElist(numbs))