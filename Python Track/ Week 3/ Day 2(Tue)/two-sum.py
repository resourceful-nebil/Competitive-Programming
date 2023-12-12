class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # To store val of nums: with there index
        numMap = {}
        # To store the indexes
        result = []

        # to iterate over the hashmap and find the complement that brings the target and return there indexes else store the number in the hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                result.append(numMap[complement])
                result.append(i)
                break
            numMap[nums[i]] = i

        return result