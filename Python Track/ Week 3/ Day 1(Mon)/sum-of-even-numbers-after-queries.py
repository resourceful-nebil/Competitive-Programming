class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        current_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for val,index in queries:
            if nums[index] % 2 == 0:
                current_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                current_sum += nums[index]

            result.append(current_sum)

        return result


