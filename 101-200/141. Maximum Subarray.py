class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maximum = float("-inf")
        n = len(nums)
        total = 0
        
        for i in range(0, n):
            total += nums[i]
            maximum = max(total, maximum)
            if total < 0:
                total = 0
        return maximum