class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n <= 2:
            return []
        ans = []

        is_prime: list[bool] = [True for _ in range(n)]    
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i <= n: 
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False                
                    j += i

            i += 1
        
        prime = []
        for i,flag in enumerate(is_prime):
            if flag == True:
                prime.append(i)
        
        # print(prime)

        l, r = 0, (len(prime) - 1)

        while l <= r:
            if prime[l] + prime[r] == n:
                ans.append([prime[l],prime[r]])
                l += 1
                r -= 1
            elif prime[l] + prime[r] < n:
                l += 1
            else:
                r -= 1
        


            # if prime[i] + prime[i + 1] == n:
            #     ans.append([prime[i],prime[i+1]])
            # elif 2*prime[i] == n:
            #     ans.append([prime[i],prime[i]])
        
        return ans 



        
