class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        for i in range(len(str(x))):
            total += int(str(x)[i])
        if x % total == 0:
            return total
        else:
            return -1