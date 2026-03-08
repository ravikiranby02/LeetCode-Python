class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []

        for c in candies:
            result.append(c + extraCandies >= maxCandies)

        return result