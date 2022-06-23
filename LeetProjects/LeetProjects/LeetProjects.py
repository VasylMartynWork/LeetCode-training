operation = ["++X","++X","X++"]
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operat in operations:
            if(operat == "x++" or operat == "++x" or operat == "X++" or operat == "++X"): x += 1
            elif(operat == "x--" or operat == "--x" or operat == "X--" or operat == "--X"): x -= 1
            else:
                return "Array's element isn't correct"
        return x

sol = Solution()
print(sol.finalValueAfterOperations(operation))