class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pair_count = 0
      
        for i, source_word in enumerate(words):
            for target_word in words[i + 1:]:
                pair_count += target_word.endswith(source_word) and target_word.startswith(source_word)
      
        return pair_count