class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s[0], s[1], s[2], s[3], s[4]

        result = []

        for col in range(ord(c1), ord(c2) + 1):
            for row in range(int(r1), int(r2) + 1):
                result.append(chr(col) + str(row))

        return result