class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        res = 0
        i = 0
        while(i < len(startTime)):
            if(startTime[i] <= queryTime <= endTime[i]):
                res += 1
            i += 1
        return res