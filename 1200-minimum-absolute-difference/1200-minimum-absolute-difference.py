class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minAbs = findmin(arr)
        i = 0
        res = []
        while(i < len(arr) - 1):
            if(arr[i + 1] - arr[i] == minAbs):
                res += [[arr[i], arr[i + 1]]]
            i += 1
        return res

def findmin(nums: list[int]) -> int:
    nums.sort()
    i = 0
    res = []
    while i < len(nums) - 1:
        res.append(nums[i + 1] - nums[i])
        i += 1
    return min(res)