"""Find Minimum Operations to Make All Elements Divisible by Three"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation = 0
        for num in nums:
            if num % 3 != 0:
                operation += 1
        return operation