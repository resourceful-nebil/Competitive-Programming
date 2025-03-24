class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        prev_end = 0

        for start,end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            days -= max(length,0)
            prev_end = max(prev_end,end) 

            
        return days
