class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                cnt += 1
        
        return cnt
