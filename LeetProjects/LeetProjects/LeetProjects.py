gain = [-5,1,5,0,-7]

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = []
        for i in range(len(gain) + 1):
            res.append(sum(gain[0:i]))
        return max(res)

sol = Solution()
print(sol.largestAltitude(gain))