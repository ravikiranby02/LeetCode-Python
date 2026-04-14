class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            mini = min(nums)
            mini_index = nums.index(mini)
            nums[mini_index] = nums[mini_index] * multiplier
            k -= 1
        
        return nums