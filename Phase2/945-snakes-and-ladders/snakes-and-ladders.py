class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def inToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n

            if r % 2:
                c = n - 1 - c

            return [r,c]
        
        q = deque()
        q.append([1,0]) # square,steps

        visited = set()

        while q:
            for _ in range(len(q)):
                square, steps = q.popleft()

                for i in range(1,7):
                    nxt = square + i
                    r,c = inToPos(nxt)

                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt == n * n:
                        return steps + 1
                    
                    if nxt not in visited:
                        q.append([nxt,steps+1])
                        visited.add(nxt)
        return -1