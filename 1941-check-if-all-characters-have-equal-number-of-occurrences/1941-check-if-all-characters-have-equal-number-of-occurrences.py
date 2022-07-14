s = "aaabb"

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        yea = 0
        yae = s.count(s[0])
        for i in s:
            yea = s.count(i)
            if(yea != yae):
                return False
        return True