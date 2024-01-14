class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        max_count = 0
        count = [0, 0]

        l = 0
        for r in range(len(answerKey)):
            count[answerKey[r] == 'T'] += 1
            max_count = max(max_count, count[answerKey[r] == 'T'])

            while max_count + k < r - l + 1:
                count[answerKey[l] == 'T'] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
