jewel = "z"
stone = "ZZ"
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numJew = 0
        for jew in jewels:
            numJew += stones.count(jew)
        return numJew

sol = Solution()
print(sol.numJewelsInStones(jewel, stone))
        