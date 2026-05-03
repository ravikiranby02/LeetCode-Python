class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_upto(x):
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            else:
                return 0
        
        s = start // 2
        e = s + n - 1
        
        result = xor_upto(e) ^ xor_upto(s - 1)
        
        # If start is odd, adjust result
        if start % 2 == 1:
            result = result * 2 + (n % 2)
        else:
            result = result * 2
        
        return result