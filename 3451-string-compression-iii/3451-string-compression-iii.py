class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        n = len(word)
        i = 0

        while i < n:
            current_char = word[i]
            count = 1  # Start with 1 for the current character
            
            # Count consecutive characters
            while i + 1 < n and word[i + 1] == current_char:
                count += 1
                i += 1

            # Append character and count to the result
            if count > 9:
                while count > 9:
                    res.append('9')
                    res.append(current_char)
                    count -= 9
            if count > 0:
                res.append(str(count))
                res.append(current_char)
            
            # Move to the next new character
            i += 1

        return ''.join(res)
