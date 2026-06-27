class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high + 1):
            s = str(n)
            mid = len(s) // 2

            if len(s) % 2 == 1:
                continue

            left = sum(int(ch) for ch in s[:mid])
            right = sum(int(ch) for ch in s[mid:])

            if left == right:
                count += 1
            
        return count