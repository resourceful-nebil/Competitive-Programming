class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        max_heap = [-1*pile for pile in piles]
        heapify(max_heap)
        # print(max_heap)
        for i in range(k):
            tmp = -heappop(max_heap)
            tmp = (ceil(tmp / 2))
            heappush(max_heap,-tmp)
        

        return -sum(max_heap)
            
