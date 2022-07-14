class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = list(str(num))
        a.reverse()
        b = int("".join(a))
        b = list(str(b))
        b.reverse()
        c = int("".join(b))
        if(c == num):
            return True
        return False