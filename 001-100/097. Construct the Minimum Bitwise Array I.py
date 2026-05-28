class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:

            # Even numbers cannot be formed
            if n % 2 == 0:
                ans.append(-1)
                continue

            bit = 1

            # Find first 0 bit from right
            while n & bit:
                bit <<= 1

            ans.append(n ^ (bit >> 1))

        return ans