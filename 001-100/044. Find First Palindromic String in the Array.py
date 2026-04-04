class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for name in words:
            if name == name[::-1]:
                return name
        return ""