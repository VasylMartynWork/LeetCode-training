start = 10
goal = 7

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        star = toBin(start)
        goa = toBin(goal)
        res = ""
        co = 0
        i = 0
        if(start > goal):
            goa = Dop(goa, len(star))
            while(i < len(goa)):
                if(goa[i] == star[i]):
                    res += star[i]
                else:
                    res += goa[i]
                    co += 1
                i += 1
        else:
            star = Dop(star, len(goa))
            while(i < len(star)):
                if(star[i] == goa[i]):
                    res += goa[i]
                else:
                    res += star[i]
                    co += 1
                i += 1
        return co

def toBin(n: int) -> str:
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
 
    return b

def Dop(n: str, num: int) -> str:
    i = 0
    st = ""
    while(i < num - len(n)):
        st += "0"
        i += 1
    st += n
    return st

sol = Solution()
print(sol.minBitFlips(start, goal))