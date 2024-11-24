class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heappop(maxHeap) * -1
            y = heappop(maxHeap) * -1

            if x != y:
                heappush(maxHeap,-(x - y))

        return -1 * maxHeap[0] if maxHeap else 0