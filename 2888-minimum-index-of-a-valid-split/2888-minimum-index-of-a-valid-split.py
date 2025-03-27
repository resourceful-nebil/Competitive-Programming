class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = 0
        cnt = 0
        for key,val in count.items():
            if val > cnt:
                cnt = val
                dominant =key
        
        left_cnt = 0
        right_cnt = cnt
        
        for i in range(len(nums)):
            if nums[i] == dominant:
                left_cnt += 1
                right_cnt -= 1
            
            left_len = i + 1
            right_len = len(nums) - 1 - i
            if 2 * left_cnt > left_len and 2 * right_cnt > right_len:
                return i
        
        return -1
        