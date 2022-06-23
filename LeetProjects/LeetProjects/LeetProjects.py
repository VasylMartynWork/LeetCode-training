nums = [2,5,1,3,4,7]
d = 3

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        nums1 = nums[:n]
        nums2 = nums[n:2*n]
        shuffled = []
        i = 0
        while(i < len(nums1)):
            shuffled.append(nums1[i])
            shuffled.append(nums2[i])
            i += 1
        return shuffled

sol = Solution()
print(sol.shuffle(nums, d))