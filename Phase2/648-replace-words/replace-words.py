class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(word):
            curr = self.root
            for ch in word:
                node = ord(ch) - ord('a')
                if node not in curr.children:
                    curr.children[node] = TrieNode()
            
                curr = curr.children[node]
            curr.is_end = True 
            curr.word = word
        def search(word):
            ans = []
            curr = self.root
            for ch in word:
                node = ord(ch) - ord('a')

                if node not in curr.children:
                    return word
                curr = curr.children[node]
                ans.append(ch)
                if curr.is_end:
                    return ''.join(ans)
            return word
        
        for w in dictionary:
            insert(w)
        
        sent = list(sentence.split())

        res = []
        for s in sent:
            a = search(s)
            res.append(a)

        return ' '.join(res)

