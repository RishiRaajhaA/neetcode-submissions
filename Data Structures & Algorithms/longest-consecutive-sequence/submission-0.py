class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        l = 0
        for x in nums_s:
            if (x - 1) not in nums_s:
                c = x
                ln = 1
                while (c + 1) in nums_s:
                    c += 1
                    ln += 1
                l = max(ln, l)
        return l