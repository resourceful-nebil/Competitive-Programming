class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
    
        def grammer(n,k):

            if n == 1:
                return 0
            
            val = grammer(n-1,ceil(k / 2))

            if k % 2 == 0:
                val += 1
            
            return val
        
        s = grammer(n,k)
        if s % 2 == 0:
            return 0
        else:
            return 1
        






        # def grammer(n):
        #     if n == 1:
        #         return "0"
            
        #     val = grammer(n-1)
        #     prevArr = ""

        #     for i in range(len(val)):
        #         if val[i] == "0":
        #             prevArr += "01"
        #         else:
        #             prevArr += "10"
        #     return prevArr

        # s = grammer(n)
        # return int(s[k - 1] )

        




        

        

        