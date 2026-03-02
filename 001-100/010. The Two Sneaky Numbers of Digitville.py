"""The Two Sneaky Numbers of Digitville"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicates = []
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicates.append(nums[i])
                
        return duplicates
