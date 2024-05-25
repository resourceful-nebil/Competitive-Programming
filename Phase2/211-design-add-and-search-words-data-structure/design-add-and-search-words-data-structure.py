class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for val in word:
            if val not in current.children:
                current.children[val] = TrieNode()
            current = current.children[val] 
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        
        def dfs(current, word):
            for i, val in enumerate(word):
                if val not in current.children and val != ".":
                    return False
                    
                elif val == ".":
                    for curr in current.children.values():
                        if dfs(curr, word[i+1:]):
                            return True
                    return False

                else:
                    current = current.children[val]

            return current.is_end

        return dfs(current, word)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
