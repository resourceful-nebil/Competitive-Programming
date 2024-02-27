class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                d = i - stack[-1] - 1
                bd = min(height[i], height[stack[-1]]) - height[top]
                water += d * bd

            stack.append(i)

        return water
        