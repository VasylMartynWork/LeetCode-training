coordinates = "h3"

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
        a = alph.index(coordinates[0]) + 1 + int(coordinates[1])
        if(a % 2 == 1):
            return True
        else:
            return False

sol = Solution()
print(sol.squareIsWhite(coordinates))