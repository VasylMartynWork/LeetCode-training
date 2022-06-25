encode = [1,2,3]
firs = 1
class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]
        for en in encoded:
            arr.append(en ^ first)
            first = en ^ first
        return arr

sol = Solution()
print(sol.decode(encode, firs))
