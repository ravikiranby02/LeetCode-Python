class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        v = {}
        c = {}
        
        for ch in s:
            d = v if ch in vowels else c
            d[ch] = d.get(ch, 0) + 1
        
        return max(v.values(), default=0) + max(c.values(), default=0)