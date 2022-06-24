candie = [4,2,1,1,2]
extraCandie = 1

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n = len(candies)
        result = [0] * n
        newCandie = [0] * n
        i = 0
        j = 0
        while(i < n):
            newCandie[i] = candies[i] + extraCandies
            j = 0
            while(j < n):
                if(newCandie[i] > candies[j] or newCandie[i] == candies[j]):
                    result[i] = True
                else:
                    result[i] = False
                    break
                j += 1
            i += 1
        return result

sol = Solution()
print(sol.kidsWithCandies(candie, extraCandie))