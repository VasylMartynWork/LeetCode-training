rectangles = [[2,3],[3,7],[4,3],[3,7]]

class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        res = []
        for i in rectangles:
            maxi = min(i)
            res.append(maxi)
        maxim = max(res)
        return res.count(maxim)

sol = Solution()
print(sol.countGoodRectangles(rectangles))