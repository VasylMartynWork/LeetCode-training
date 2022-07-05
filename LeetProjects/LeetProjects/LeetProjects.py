words = ["abc","car","ada","racecar","cool"]

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in words:
            a = list(i)
            b = []
            b += a
            b.reverse()
            if(a == b):
                return i
        return ""
            
sol = Solution()
print(sol.firstPalindrome(words))