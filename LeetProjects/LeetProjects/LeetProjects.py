numbers = [1,2,3,4]

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        try:
            runningSim = [0] * len(nums)
            i = 0
            while(i < len(nums)):
                runningSim[i] = sumOfNumbers(nums, i)
                i += 1
            return runningSim
        except:
            return "Array isn't correct"

def sumOfNumbers(numbes: list[int], iter: int) -> int:
    summ = 0
    j = 0
    while(j <= iter):
        summ += numbes[j]
        j += 1

    return summ