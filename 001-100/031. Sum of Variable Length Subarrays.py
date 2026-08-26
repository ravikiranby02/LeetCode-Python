class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefix = [0] * n
        prefix[0] = nums[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        total = 0
        
        for i in range(n):
            start = max(0, i - nums[i])         
            if start > 0:
                total += prefix[i] - prefix[start - 1]
            else:
                total += prefix[i]
        return total
