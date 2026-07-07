class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i])
            ans.append(word2[i])

        ans.append(word1[len(word2):])
        ans.append(word2[len(word1):])

        return "".join(ans)