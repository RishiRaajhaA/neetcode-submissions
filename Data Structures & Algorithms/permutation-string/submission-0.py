class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}
        count2 = {}
        l = 0
        for ch in s1:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        for i in range(len(s1)):
            ch = s2[i]
            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1
        if count1 == count2:
            return True
        while l + len(s1) < len(s2):
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            ch = s2[l + len(s1)]
            count2[ch] = count2.get(ch, 0) + 1
            l += 1
            if count1 == count2:
                return True
        return False