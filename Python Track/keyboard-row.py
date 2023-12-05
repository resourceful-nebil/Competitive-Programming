class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
            'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
        }       
        result=[]
        for word in words:
            small = word.lower()

            row = rows[small[0]]
            if all(rows[ch] == row for ch in small):
                result.append(word)
        return result

