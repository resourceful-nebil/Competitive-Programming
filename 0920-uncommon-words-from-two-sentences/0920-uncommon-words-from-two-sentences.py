class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        
        words = {}
        
        for word in s1:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        
        for word in s2:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        
        uncommon = []
        
        for word in words:
            if words[word] == 1:
                uncommon.append(word)
        
        return uncommon
        