from audioop import reverse

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=secEl, reverse = True)
        res = 0
        for i in boxTypes:
           if(i[0] <= truckSize):
              res += i[0] * i[1]
              truckSize -= i[0]
              if(truckSize == 0):
                  break
           elif(i[0] > truckSize):
                res += truckSize * i[1]
                return res
        return res

def secEl(el):
    return el[1]