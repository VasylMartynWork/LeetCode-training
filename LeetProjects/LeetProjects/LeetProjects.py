word = "xyxzxe"
ch = ""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            a = word.index(ch)
        except:
            return word
        b = word[0:a + 1]
        b = list(b)
        b.reverse()
        res = "".join(b)
        #s = res + word[len(res):len(word)]
        return res + word[len(res):len(word)]

sol = Solution()
print(sol.reversePrefix(word, ch))