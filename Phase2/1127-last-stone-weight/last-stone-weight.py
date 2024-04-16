class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones] 
        
        heapify(stones)

        while len(stones) > 1:
            y = heappop(stones)
            y *= -1
            x = heappop(stones)
            x *= -1

            if x == y:
                continue
            
            heappush(stones,x-y)

        # stones = [i*-1 for i in stones] 
        return -stones[0] if stones else 0
