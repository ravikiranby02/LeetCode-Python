class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n

        freq = [0] * (N + 1)

        for row in grid:
            for num in row:
                freq[num] += 1

        repeated = missing = 0

        for num in range(1, N + 1):
            if freq[num] == 2:
                repeated = num
            elif freq[num] == 0:
                missing = num

        return [repeated, missing]