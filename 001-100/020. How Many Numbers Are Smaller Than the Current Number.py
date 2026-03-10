class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        count = [0] * n

        for i in range(n):
            total = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    total += 1
            count[i] = total
        return count