class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        dis = arr[1] - arr[0]
        i = 0
        res = True
        while i < len(arr) - 1:
            if(arr[i + 1] - arr[i] != dis):
                res = False
            i += 1
        return res