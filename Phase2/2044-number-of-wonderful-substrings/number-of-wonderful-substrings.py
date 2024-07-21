class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask_counter = Counter({0:1})
        cnt = 0
        st = 0

        for c in word:
            st ^= 1 << (ord(c) - ord('a'))
            cnt += mask_counter[st]

            for i in range(10):
                cnt += mask_counter[st  ^ (1 << i)]
            
            mask_counter[st] += 1
        
        return cnt 