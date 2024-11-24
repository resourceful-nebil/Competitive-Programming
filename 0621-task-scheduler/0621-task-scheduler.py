class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        time = 0
        maxHeap = [-c for c in cnt.values()]
        heapq.heapify(maxHeap)

        q = deque() # [cnt,time]
        while maxHeap or q:
            time += 1

            if maxHeap:
                c = 1 + heappop(maxHeap) 
                if c:
                    q.append([c,time + n])
            
            if q and q[0][1] == time:
                heappush(maxHeap,q.popleft()[0])
        
        return time

                


            