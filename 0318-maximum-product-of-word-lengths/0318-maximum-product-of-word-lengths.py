class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maskDict = {}
        n = len(words)

        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
                # print(bitmask,char)
            maskDict[word] = bitmask

        # print(maskDict)
        maxProduct = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if maskDict[words[i]] & maskDict[words[j]] == 0:
                    product = len(words[i]) * len(words[j])
                    maxProduct = max(maxProduct, product)

        return maxProduct