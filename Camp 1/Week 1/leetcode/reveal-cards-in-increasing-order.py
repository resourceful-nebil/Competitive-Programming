class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse=True)

        for d in range(len(deck)):
            if not queue:
                queue.append(deck[d])
            else:
                x = queue.popleft()
                queue.append(x)
                queue.append(deck[d])
            
        return list(queue)[::-1]



            