class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sent = list(map(str,sentence.split(' ')))
        print(sent)
        if sent[0][0] != sent[-1][-1]:
                # print(sent[i],"1____")
                return False
        for i in range(len(sent)):  
            if i > 0 and sent[i][0] != sent[i - 1][-1]:
                # print(sent[i],"2____")
                return False
        
        return True