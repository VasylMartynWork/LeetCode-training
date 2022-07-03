s = "a1c1e1"

class Solution:
    def replaceDigits(self, s: str) -> str:
        alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z"]
        i = 0
        res = ""
        while(i < len(s)):
            st = s[i:i+2]
            res += st[0]
            try:
                res += alph[alph.index(st[0]) + int(st[1])]
            except:
                pass
            i += 2
        return res

sol = Solution()
print(sol.replaceDigits(s))