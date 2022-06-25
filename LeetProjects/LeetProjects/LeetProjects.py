comm = "G()(al)"
class Solution:
    def interpret(self, command: str) -> str:
        com = command.replace("()", "o").replace("(", "").replace(")", "").replace("(al)", "al")
        return com

sol = Solution()
print(sol.interpret(comm))