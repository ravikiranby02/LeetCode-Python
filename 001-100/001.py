"""Restore Finishing Order"""

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        rk = []
        for i in order:
            for j in friends:
                if i == j:
                    rk.append(i)
        return rk