class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in D:
                return [D[complement], i]
            D[nums[i]] = i