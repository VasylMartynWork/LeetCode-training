account = [[1,5],[7,3],[3,5]]
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for acc in accounts:
            if(sum(acc) > richest): richest = sum(acc)
        return richest

sol = Solution()
print(sol.maximumWealth(account))