class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        res = bin(res)
        res = res[2:]
        cnt = Counter(res)
        # print(cnt)
        return cnt['1']