s = "eOEvoOAfOIIi"

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[0:int(len(s) / 2)]
        b = s[int(len(s) / 2):len(s)]
        one = 0
        two = 0
        for i in vowel:
            yea = i in a
            yae = i in b
            if(yea == True):
                one += a.count(i)
            if(yae == True):
                two += b.count(i)
        if(one == two):
            return True
        else:
            return False

sol = Solution()
print(sol.halvesAreAlike(s))