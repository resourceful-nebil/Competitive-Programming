class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf')] * n 
        prev[src] = 0

        for i in range(k + 1):
            temp = prev[:]
            
            for s,d,p in flights:
                if prev[s] == float('inf'):
                    continue
                if prev[s] + p < temp[d]:
                    temp[d] = prev[s] + p
            prev = temp
        
        return -1 if prev[dst] == float('inf') else prev[dst]
