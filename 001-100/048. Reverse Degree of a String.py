class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        
        for i, ch in enumerate(s):
            reverse_value = 26 - (ord(ch) - ord('a'))
            result += reverse_value * (i + 1)
        
        return result