class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(list(word))
        res = 0
      
        sorted_counts = sorted(cnt.values(), reverse=True)
        # print(sorted_counts)
        for idx, count in enumerate(sorted_counts):
            
            res += ((idx // 8) + 1) * count
      
        return res

