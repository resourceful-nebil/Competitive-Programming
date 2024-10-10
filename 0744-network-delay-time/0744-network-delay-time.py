class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        processed = set()
        t = 0

        for u,v,w in times:
            edges[u].append((v,w))
        

        heap = [(0, k)]
        while heap:
            dist, node = heappop(heap)
            if node in processed:
                continue
            
            processed.add(node)
            t = max(t,dist)
            
            for child,distance in edges[node]:
                cur_dist = dist + distance 
                if child not in processed:
                    heapq.heappush(heap,(cur_dist,child))
            
                    
        return t if len(processed) == n else -1