"""Minimum Operations to Make Array Sum Divisible by K"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % k
        return remainder
