class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        D = {}
        for ch in s:
            if ch not in D:
                D[ch] = 1
            else:
                D[ch] += 1
        for ch in t:
            if ch not in D:
                return False
            D[ch] -= 1
            if D[ch] < 0:
                return False
        return True