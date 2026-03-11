class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        result = []
        for i in nums:
            running_sum += i
            result.append(running_sum)
        return result