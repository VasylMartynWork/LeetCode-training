word1 = ["ab", "c"]
word2 = ["a", "bc"]

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        wo1 = ""
        wo2 = ""
        for i in word1:
            wo1 += i
        for j in word2:
            wo2 += j
        if(wo1 == wo2):
            return True
        else:
            return False

sol = Solution()
print(sol.arrayStringsAreEqual(word1, word2))

