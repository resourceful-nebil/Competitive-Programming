class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counted_nums = Counter(nums)

        result_sum = 0

        for num, freq in counted_nums.items():
            if freq == 1:
                result_sum += num

        return result_sum
 