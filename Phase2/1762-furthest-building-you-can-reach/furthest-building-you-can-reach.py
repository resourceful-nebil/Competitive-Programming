class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        diff = []
        for i in range(len(heights) - 1):
            diff.append(heights[i + 1] - heights[i])
        
        i = 0
        heap = []
        for j in range(len(diff)):
            # print(i)
            if diff[j] > 0:
                heappush(heap,diff[j])
            if len(heap) > ladders and bricks >= 0:
                min_ = heappop(heap)
                if bricks < min_:
                    break
                bricks -= min_

            i += 1            
            


        
        # print(diff)
        # i += 1
        return i 


        
