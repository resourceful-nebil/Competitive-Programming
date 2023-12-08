class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        ans = []

        # the use of lambda fun to arrange array 
        nums = sorted(nums, key = lambda x: x<0)
        length = len(nums)//2
        for i in range(length):
            ans.append(nums[i])
            ans.append(nums[i+length])

        return ans
