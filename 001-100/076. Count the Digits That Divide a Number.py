class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        count = 0
        while num > 0:
            d = num % 10
            if d != 0 and original % d == 0:
                count += 1
            num //= 10
        return count