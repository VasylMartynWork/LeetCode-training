target = [1,2,3,4]
arr = [2,4,1,3]

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        arr.sort()
        target.sort()
        if(target == arr):
            return True
        else:
            return False

sol = Solution()
print(sol.canBeEqual(target, arr))