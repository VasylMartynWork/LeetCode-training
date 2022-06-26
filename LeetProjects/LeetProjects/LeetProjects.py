st = "P7:Z7"
class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                    "S", "T", "U", "V", "W", "X", "Y", "Z"]
        stri = s.split(":")
        des = int(stri[1][1]) - int(stri[0][1])
        i = alphabet.index(stri[0][0])
        res = []
        while(i <= alphabet.index(stri[1][0])):
            j = int(stri[0][1])
            while(j <= int(stri[1][1])):
                stro = alphabet[i]
                stro += str(j)
                res.append(stro)
                j += 1
            if(des == 0):
                i += des + 1
            else:
                i += 1
        return res

sol = Solution()
print(sol.cellsInRange(st))