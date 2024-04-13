class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        

        q = deque()
        q.append(["0000",0])

        visited = set(deadends)

        while q:
            node,turn = q.popleft()

            if node == target:
                return turn

            for child in children(node):
                if child not in visited:
                    q.append([child,turn + 1])
                    visited.add(child)
                
        return -1
            

                




        