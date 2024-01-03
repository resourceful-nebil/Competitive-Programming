class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the list of skill levels in ascending order
        skill.sort()
        
        i = 1  # Pointer for the second player
        j = len(skill) - 2  # Pointer for the second-to-last player

        # Calculate the sum of the skill levels of the first and last players
        s = skill[0] + skill[-1]

        # Calculate the initial product of the skill levels of the first and last players
        ans = skill[0] * skill[-1]

        # Iterate until the pointers meet or cross each other
        while i <= j:
            # Check if the sum of the skill levels of the second and second-to-last players is equal to the sum of the first and last players
            if s != skill[i] + skill[j]:
                return -1  # If the sums are not equal, return -1 to indicate that it is not possible to divide the players
            else:
                # Add the product of the skill levels of the second and second-to-last players to the answer
                ans += skill[i] * skill[j]
                i += 1  # Move the second player pointer to the next player
                j -= 1  # Move the second-to-last player pointer to the previous player
        
        return ans  # Return the final answer, which represents the sum of the products of the skill levels of the paired players