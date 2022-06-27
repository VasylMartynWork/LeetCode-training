items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0
        cou = 0
        while(i < len(items)):
            if(ruleKey == "type"):
                check = 0
            elif(ruleKey == "color"):
                check = 1
            elif(ruleKey == "name"):
                check = 2
            else:
                return "Rule isn't true"
            if(items[i][check] == ruleValue):
                cou += 1
            i += 1
        return cou

sol = Solution()
print(sol.countMatches(items, ruleKey, ruleValue))