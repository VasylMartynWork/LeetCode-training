numbers = [1,2,3]
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums
        return ans
answ = Solution()
print(answ.getConcatenation(numbers))