mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        i = 0
        j = len(mat) - 1
        res = 0
        res2 = 0
        while(i < len(mat)):
            res += mat[i][i]
            i += 1
        i = 0
        while(i < len(mat)):
            if(i + 1 == (len(mat) + 1) / 2):
                i += 1
                j -= 1
                continue
            res2 += mat[i][j]
            i += 1
            j -= 1
        return res + res2

sol = Solution()
print(sol.diagonalSum(mat))