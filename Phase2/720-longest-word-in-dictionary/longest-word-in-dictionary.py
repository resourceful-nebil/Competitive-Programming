class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:
        def insert(word):
            curr = self.root
            for ch in word:
                node = ord(ch) - ord('a')
                if node not in curr.children:
                    curr.children[node] = TrieNode()
            
                curr = curr.children[node]
            curr.is_end = True 
            curr.word = word
        
        for w in words:
            insert(w)
        
        ans = []
        def bfs(words):
            node = self.root
            q = deque()

            q.append(node)
            while q:
                node = q.pop()
                # print(node.children)
               
                for next in node.children:
                    # print(next,node.word)
                    if node.children[next].is_end:
                        ans.append(node.children[next].word)
                    
                        q.append(node.children[next])

            

        bfs(words)
        ans.sort()
        x = ans[0] if ans else ""
        for a in ans:
            if len(a) > len(x):
                x = a
        return x
        # print(ans)



        


        