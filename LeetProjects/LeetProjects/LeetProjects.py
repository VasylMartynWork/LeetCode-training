s = "Hello how are you Contestant"
k = 4

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st = s.split()
        i = 0
        stri = ""
        while(i < k):
            stri += st[i]
            if(i < k - 1):
                stri += " "
            i += 1
        return stri

sol = Solution()
print(sol.truncateSentence(s, k))