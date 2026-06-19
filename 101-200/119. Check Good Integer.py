class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0
        for i in range(len(str(n))):
            digitSum += int(str(n)[i])
            squareSum += int(str(n)[i]) ** 2
        if squareSum - digitSum >= 50:
            return True
        else:
            return False