class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        rightBest = -inf

        for num in nums[::-1]:
            if num < rightBest:
                return True 
            while stack and num > stack[-1]:
                x = stack.pop()
                rightBest = x
            stack.append(num)
        
        return False