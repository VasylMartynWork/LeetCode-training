class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for i in arr1:
            a = 0
            for j in arr2:
                if abs(i - j) <= d:
                    a += 1
                    break
            if(a == 1):
                a = 0
            else:
                res += 1
        return res
