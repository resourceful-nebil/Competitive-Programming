class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(_min):
            prev_pos = position[0]
            count = 1
            for cur_pos in position[1:]:
                if cur_pos - prev_pos >= _min:
                    prev_pos = cur_pos
                    count += 1
            return count >= m

        position.sort()
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2  
            if helper(mid):
                left = mid
            else:
                right = mid - 1
      
        return left