image = [[1,1,0],[1,0,1],[0,0,0]]

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = []
        for i in image:
            i.reverse()
            resu = []
            for j in i:
                if(j == 1):
                    j = 0
                elif(j == 0):
                    j = 1
                
                resu.append(j)
            res.append(resu)
        return res

sol = Solution()
print(sol.flipAndInvertImage(image))