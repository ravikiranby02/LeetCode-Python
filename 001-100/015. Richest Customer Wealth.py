class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = []
        for i in accounts:
            r.append(sum(i))
        return max(r)