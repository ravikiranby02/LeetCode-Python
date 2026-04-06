class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        specials = []

        # Collect
        for c in s:
            if c.islower():
                letters.append(c)
            else:
                specials.append(c)

        # Reverse
        letters.reverse()
        specials.reverse()

        # Rebuild
        res = []
        i = j = 0

        for c in s:
            if c.islower():
                res.append(letters[i])
                i += 1
            else:
                res.append(specials[j])
                j += 1

        return "".join(res)