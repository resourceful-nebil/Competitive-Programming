class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        di = {}
        c = 0

        for i in range(len(s)):
            if s[i] == '|':
                di[i] = c
            else:
                c += 1
        if not di:
            return [0] * len(queries)
        print(di)
        
        arr = []
        for i in range(len(s)):
            if s[i] == '|':
                arr.append(i)
        # print(arr)
        
        ans = []
        for i in range(len(queries)):
            left = bisect_left(arr,queries[i][0])
            if left == len(arr):
                left -=1
            right = bisect_right(arr,queries[i][1]) - 1
            if right < 0:
                right = 0
        
            diff = di[arr[right]] - di[arr[left]] 
            if diff < 0: 
                diff = 0
            ans.append(diff)
        
        return ans
            
            