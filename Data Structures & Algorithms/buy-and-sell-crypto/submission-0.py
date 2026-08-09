class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_pr = 0
        while r < len(prices):
            pr = prices[r] - prices[l]
            if pr > max_pr:
                max_pr = pr
            else:
                if prices[r] < prices[l]:
                    l = r
            r += 1
        return max_pr