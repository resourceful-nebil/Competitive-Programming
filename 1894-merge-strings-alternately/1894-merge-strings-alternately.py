class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        i=0
        j=0
        ans=[]

        while i < len1 and j < len2:
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        ans.append(word1[i:])
        ans.append(word2[j:])
        return ''.join(ans) 
