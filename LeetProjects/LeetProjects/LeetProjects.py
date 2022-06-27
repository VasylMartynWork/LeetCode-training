n = 5
start = 0

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        i = 0
        xor = 0
        while(i < n):
            nums.append(start + 2 * i)
            xor = xor ^ nums[i]
            i += 1

        return xor

sol = Solution()
print(sol.xorOperation(n, start))