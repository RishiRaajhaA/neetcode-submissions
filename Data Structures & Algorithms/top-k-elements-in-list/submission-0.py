class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        L = []
        for i in range(len(nums)):
            if nums[i] not in D:
                D[nums[i]] = 1
            else:
                D[nums[i]] += 1
        Ds = dict(sorted(D.items(), key=lambda item: item[1], reverse = True))
        x = list(Ds.keys())
        for i in range(k):
            L.append(x[i])
        return L