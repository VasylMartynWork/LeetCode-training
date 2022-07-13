left = 1
right = 22

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        i = left
        res = []
        while(i <= right):
            if(nada(i) == True):
                b = list(str(i))
                af = True
                for j in b:
                    if(i % int(j) != 0):
                        af = False
                if(af == True):
                    res.append(i)
                i += 1
            else:
                i += 1
                continue
        return res

def nada(num: int) -> bool:
    res = True
    n = list(str(num))
    for i in n:
        if(i == "0"):
            res = False
    return res