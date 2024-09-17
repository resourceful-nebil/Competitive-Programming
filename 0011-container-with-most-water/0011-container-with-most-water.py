class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        res = 0
        cur_height = 0
        while l < r:
            cur_height = (r - l) * min(height[l],height[r])
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            res = max(res,cur_height)
        
        return res 
