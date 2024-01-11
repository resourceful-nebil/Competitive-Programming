class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        last_index = defaultdict(int)

        for i in range(len(cards)):
            if cards[i] in last_index:
                ans = min(ans, i - last_index[cards[i]] + 1)
            last_index[cards[i]] = i

        return -1 if ans == float('inf') else ans            
            
