class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores = [0]

        for c in s:
            if c == '(':
                scores.append(0)
            else:
                topScore = scores.pop()
                previousScore = scores.pop()

                currentScore = previousScore + max(topScore * 2, 1)
                scores.append(currentScore)

        return scores[-1]