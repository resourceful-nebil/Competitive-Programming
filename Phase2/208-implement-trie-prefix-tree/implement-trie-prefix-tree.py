class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            node = ord(ch) - ord('a')
            if not curr.children[node]:
                curr.children[node] = TrieNode()
        
            curr = curr.children[node]
        curr.is_end = True 
        
    def search(self, word: str) -> bool:
        cur = self.root 
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        
        if cur.is_end:
            return True
        else:
            return False 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
            
        return True  
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)