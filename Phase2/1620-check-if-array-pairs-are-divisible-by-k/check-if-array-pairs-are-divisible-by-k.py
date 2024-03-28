class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        for i in range(n):
            arr[i] %= k
        
        di = Counter(arr)
        count = 0

        # 000
        if di[0] % 2 == 1:
            return False 
        

        for i in range(1,k):
            diff = k - i
            if di[diff] != di[i]:
                return False
        # print(count)

        return True 


        

        
