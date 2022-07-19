class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in nums2:
            a = i in nums1
            if a == True:
                b = i in res
                if b == False:
                    res.append(i)
        return res