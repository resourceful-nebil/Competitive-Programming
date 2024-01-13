class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    ans = 0
    max_count = 0
    count = collections.Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      max_count = max(max_count, count[c])
      while max_count + k < r - l + 1:
        count[s[l]] -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans