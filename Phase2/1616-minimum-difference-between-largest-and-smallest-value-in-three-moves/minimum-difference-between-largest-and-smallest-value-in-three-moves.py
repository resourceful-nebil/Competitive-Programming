class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        res = float('inf')

        min_four = (nsmallest(4,nums))
        max_four = sorted(nlargest(4,nums))
        # print(min_four)
        # print(max_four)

        for i in range(4):
            res = min(res,max_four[i] - min_four[i])


        return res