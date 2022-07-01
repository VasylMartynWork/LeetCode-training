rings = "G4"

class Solution:
    def countPoints(self, rings: str) -> int:
        rg = ["R", "G", "B"]
        i = 0
        res = 0
        while(i < 10):
            co = 0
            for j in rg:
                exist = f"{j}{i}" in rings
                if(exist == True):
                    co += 1
                else:
                    co = 0
            if(co == 3):
                res += 1
            i += 1
        return res

sol = Solution()
print(sol.countPoints(rings))