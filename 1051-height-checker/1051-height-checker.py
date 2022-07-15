heights = [1,1,4,2,1,3]

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = []
        expected += heights
        expected.sort()
        i = 0
        res = 0
        while(i < len(heights)):
            if(expected[i] != heights[i]):
                res += 1
            i += 1
        return res

sol = Solution()
print(sol.heightChecker(heights))