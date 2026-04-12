class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i in s:
            result += abs(s.index(i) - t.index(i))
        return result