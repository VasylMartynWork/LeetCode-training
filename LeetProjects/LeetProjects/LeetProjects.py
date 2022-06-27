arr = [1,4,2,5,3]

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        j = 1
        res = 0
        while True:
            if(j > len(arr)):
                break
            i = 0
            while(i < len(arr)):
                if(len(arr[i:i + j]) < j):
                    break
                a = arr[i:i + j]
                res += sum(a)
                i += 1
            j += 2
        return res

sol = Solution()
print(sol.sumOddLengthSubarrays(arr))