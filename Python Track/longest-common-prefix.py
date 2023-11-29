class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        front = strs[0]
        back = strs[-1]
        length = min(len(front), len(back))
        ans = ""
        i = 0

        while i < length:
            if front[i] == back[i]:
                ans += front[i]
            else:
                break
            i+=1
        return ans

