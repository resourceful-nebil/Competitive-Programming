class TrieNode:
    def __init__(self):
        self.endOfString = False
        self.children = [None, None]


class Solution:
    def __init__(self):
            self.root = TrieNode()

    def findMaximumXOR(self, nums: List[int]) -> int:
        def insert(s):
            cur = self.root
            for ch in s:
                bit = int(ch)
                if not cur.children[bit]:
                    cur.children[bit] = TrieNode()
                cur = cur.children[bit]

            cur.endOfString = True 
        
        def search(s):
            ans = ""
            cur = self.root
            for ch in s:
                # print(ch)
                bit = 1 - int(ch)
                if cur.children[bit]:
                    # print("here")
                    cur = cur.children[bit]
                    ans += '1'
                else:
                    cur = cur.children[int(ch)]
                    ans += '0'
            # print(ans)
            return int(ans,2)

        arr = []
        for num in nums:
            b = bin(num)
            val = list(b[2:] [::-1])
            # print(val)
            if len(val) < 32:
                diff = 32 - len(val)
                add_zero = [0] * diff
                val.extend(add_zero)
                val = val[::-1]
            # print(val)
            insert(val)
            arr.append(val)

        mx = 0
        for num in arr:
            mx = max(mx,search(num))
        
        return mx
        

        

        # print(self.root.children)
            # print(b[2:])














            