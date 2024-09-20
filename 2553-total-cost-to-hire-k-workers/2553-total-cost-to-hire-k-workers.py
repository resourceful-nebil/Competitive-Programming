class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minHeap = []
        n = len(costs)
        first,last = candidates - 1, n - candidates
        for h in range(candidates):
            heappush(minHeap,(costs[h],h))
        for h in range(last,n):
            if h > first:
                heappush(minHeap,(costs[h],h))
        heapify(minHeap)
        
        res = 0
        for _ in range(k):
            candi,idx = heappop(minHeap)
            res += candi

            if idx <= first:
                first += 1
                if first < last:
                    heappush(minHeap,(costs[first],first))
            if idx >= last:
                last -= 1
                if first < last:
                    heappush(minHeap,(costs[last],last))

        return res 
