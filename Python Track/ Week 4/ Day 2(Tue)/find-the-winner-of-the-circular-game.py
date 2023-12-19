class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=list(range(1,n+1))
        count=0
        i=0
        while len(nums)>1:
            count+=1
            if count==k:
                nums.pop(i)
                count=0
            else:
                i+=1
                i %= len(nums)
        return nums[-1]