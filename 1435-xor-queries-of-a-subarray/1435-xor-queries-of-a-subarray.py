class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i - 1]
        return [arr[j] ^ (arr[i - 1] if i > 0 else 0)for i,j in queries]