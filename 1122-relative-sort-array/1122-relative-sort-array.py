class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []
        for i in arr2:
            a = i in arr1
            while a == True:
                res.append(i)
                arr1.remove(i)
                a = i in arr1
        arr1.sort()
        for j in arr1:
            res.append(j)
        return res