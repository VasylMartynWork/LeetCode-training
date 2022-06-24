number = 234
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numMnoz = 1
        numDod = 0
        dig = list(str(n))
        i = 0
        while(i < len(dig)):
            numMnoz *= int(dig[i])
            numDod += int(dig[i])
            i += 1
        return numMnoz - numDod

sol = Solution()
print(sol.subtractProductAndSum(number))