n = 14

class Solution:
    def numberOfMatches(self, n: int) -> int:
        team = n
        roun = 0
        if n % 2 == 0:
            while True:
                if(team == 1):
                    break
                if(team % 2 == 1):
                    roun += (team - 1) // 2
                    team = (team - 1) // 2 + 1
                else:
                    roun += team // 2
                    team = team // 2
        else:
            while True:
                if(team == 1):
                    break
                if(team % 2 == 1):
                    roun += (team - 1) // 2
                else:
                    roun += team // 2
                team = (team - 1) // 2 + 1
        return roun

sol = Solution()
print(sol.numberOfMatches(n))