class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        for s in strs:
            x.append("".join(sorted(s)))
        D = {}
        for i in range(len(x)):
            if x[i] not in D:
                D[x[i]] = [strs[i],]
            else:
                D[x[i]].append(strs[i])
        return list(D.values())