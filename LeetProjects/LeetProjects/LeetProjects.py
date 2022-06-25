st = "codeleet"
indi = [4,5,6,7,0,2,1,3]
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        j = 0
        sorInd = []
        sorSt = ""
        while(j < len(indices)):
            it = 0
            for ind in indices:
                if(j == ind):
                    break
                it += 1
            sorInd.append(it)
            j += 1
        for a in sorInd:
            sorSt += s[a]
        return sorSt

sol = Solution()
print(sol.restoreString(st, indi))