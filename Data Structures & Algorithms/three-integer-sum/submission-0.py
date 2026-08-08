class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                value = nums[l] + nums[r] + nums[i]
                if value > 0:
                    r -= 1
                    continue
                if value < 0:
                    l += 1
                    continue
                if value == 0:
                    L.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                l += 1
                r -= 1
        return L