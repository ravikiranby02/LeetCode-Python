class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        current = 'a'
        
        # Step 1: Build mapping
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = current
                current = chr(ord(current) + 1)
        
        # Step 2: Decode message
        result = []
        for ch in message:
            if ch == ' ':
                result.append(' ')
            else:
                result.append(mapping[ch])
        
        return "".join(result)