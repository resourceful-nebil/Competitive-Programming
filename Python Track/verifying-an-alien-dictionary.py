class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        foriegn_dict = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    if foriegn_dict[word1[j]] > foriegn_dict[word2[j]]:
                        return False 
                    else:
                        break 
                else:
                    if len(word1) > len(word2) and word1[:len(word2)] == word2:
                        return False
        return True 

            