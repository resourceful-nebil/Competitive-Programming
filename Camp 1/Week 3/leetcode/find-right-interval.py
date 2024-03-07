class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i] = (intervals[i][0],intervals[i][1],i)
        
        intervals.sort()
        res = [-1] * len(intervals)

        for s,e,i in intervals:
            temp = bisect_left(intervals,(e,-inf,0))
            if temp < len(intervals):
                j = intervals[temp][2] 
                res[i] = j
        
        # print(res)
        # res = [val if val < float('inf') else -1 for val in res]
        return res