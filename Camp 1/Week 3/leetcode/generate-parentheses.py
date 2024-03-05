class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ""
        def backtrack(path,countOpen,countClosed):
            if countOpen == n and countClosed == n:
                ans.append(path)
                return
            
            if countOpen < n:
                backtrack(path + '(', countOpen + 1,countClosed)
            if countClosed < n and countClosed < countOpen:
                backtrack(path + ')', countOpen, countClosed + 1)
            
        
        backtrack(path,0,0)
        return ans

                