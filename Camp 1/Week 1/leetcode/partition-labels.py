class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        di = {}

        for i in range(len(s)):
            di[s[i]] = i
        
        current = 0
        ans = []
        while current < n:
            end = di[s[current]]
            j = current + 1

            while j < end:
                end = max(end,di[s[j]])
                j += 1
            ans.append(end - current + 1)
            current = end + 1

        return ans 