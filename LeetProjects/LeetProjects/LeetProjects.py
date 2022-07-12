words = ["pay","attention","practice","attend"]
pref = "at"

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        co = 0
        for i in words:
            if(i[0:len(pref)] == pref):
                co += 1

        return co

sol = Solution()
print(sol.prefixCount(words, pref))