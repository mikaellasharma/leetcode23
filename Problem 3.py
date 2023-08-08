# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        lss = 0
        length = len(s)
        if length < 2:
            return length
        s += s[-1]
        while j <= length:
            if len(set(s[i:j])) < len(s[i:j]):
                i += 1
            lss = max(lss, len(s[i:j]))
            j += 1
        return lss
