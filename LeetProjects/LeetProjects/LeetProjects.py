s = "Let's take LeetCode contest"

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = ""
        k = 0
        for i in arr:
            k += 1
            a = len(i) - 1
            resa = ""
            while(a >= 0):
                resa += i[a]
                a -= 1
            res += resa
            if(k < len(arr)):
                res += " "
        return res

sol = Solution()
print(sol.reverseWords(s))