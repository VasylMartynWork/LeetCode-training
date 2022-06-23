adress = "1.1.1.1.1"
class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        if(address.count(".") == 3 and address[len(address) - 1] != "."):
            for c in address:
                if(c == "."): defanged += "[.]"
                else: defanged += c
        else:
            return "This is not IPv4 address"
        return defanged

sol = Solution()
print(sol.defangIPaddr(adress))