class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set([])
        for v in nums:
            if v in x:
                return True
            else:
                x.add(v)
        return False