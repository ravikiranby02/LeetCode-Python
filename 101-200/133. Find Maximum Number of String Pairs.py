class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        total = 0
        for word in words:
            if word[::-1] in seen:
                total += 1
            else:
                seen.add(word)
        return total