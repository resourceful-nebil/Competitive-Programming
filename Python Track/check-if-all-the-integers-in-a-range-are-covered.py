class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_range = {num for num in range(left,right+1)}

        for i in (ranges):
            for j in range(i[0],i[1]+1):
                if j in new_range:
                    new_range.remove(j)
        
        if not new_range:
            return True 
        else:
            return False