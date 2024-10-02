class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        ans = set()
        
        for key,val in cnt.items():
            if val in ans:
                return False
            ans.add(val)
        
        return True