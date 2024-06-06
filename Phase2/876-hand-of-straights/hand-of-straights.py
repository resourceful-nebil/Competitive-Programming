class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Count the frequency of each card in the hand
        card_count = Counter(hand)
      
        # Sort the hand to form groups in ascending order
        for card_value in sorted(hand):
            # If the current card can start a group
            if card_count[card_value]:
                # Attempt to form a group of the specified size
                for next_card_value in range(card_value, card_value + groupSize):
                    # If the next card isn't available, the group can't be formed
                    if card_count[next_card_value] == 0:
                        return False
                    # Decrement the count of the current card forming the group
                    card_count[next_card_value] -= 1
                    # If all instances of this card have been used, remove it from the counter
                    if card_count[next_card_value] == 0:
                        card_count.pop(next_card_value)
        # If all cards can be successfully grouped, return True
        return True