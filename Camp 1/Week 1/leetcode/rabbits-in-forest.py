class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = Counter(answers)
        num = 0
        for key,val in ans.items():
            num += ceil(val/(key+1))*(key+1)
        return num