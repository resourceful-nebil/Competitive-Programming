class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        {0:[0]}
        # {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]})
        # sum of i + j:[the value] [i][j]
        result = defaultdict(list)
        ans = []

       
        # 
        for i in range(row):
            for j in range(col):
                result[i + j].append(mat[i][j])
        
        # if it is append() it returns [[1],[2,2] ...]
        # but if it is extend() it returns [[1,2...]]
        for key,value in result.items():
            if key % 2 == 0:
                ans.extend(value[::-1]) # to reverse the value list in the dict
            else:
                ans.extend(value)
        print(result)
        return ans


        
        

    


