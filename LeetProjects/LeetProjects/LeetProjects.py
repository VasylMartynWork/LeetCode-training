s = "10#11#12"

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        resa = []
        res = ""
        alph = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "j10#", "k11#", "l12#", "m13#", "n14#", "o15#",
                 "p16#", "q17#", "r18#", "s19#", "t20#", "u21#", "v22#", "w23#", "x24#", "y25#", "z26#",]
        while(i >= 0):
            if(s[i] == "#"):
                for j in alph:
                    if(s[i - 2: i] == j[1:3]):
                        resa += j[0]
                        i -= 3
                        break
            else:
                for j in alph:
                    if(s[i] == j[1]):
                        resa += j[0]
                        i -= 1
                        break
        k = len(resa) - 1
        while(k >= 0):
            res += resa[k]
            k -= 1
        return res

sol = Solution()
print(sol.freqAlphabets(s))