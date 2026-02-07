from collections import Counter
class Solution:
    def commonChars(self, words):
        count = Counter(words[0])

        for word in words[1:]:
            count &= Counter(word)
            
        result = []
        for char, counter in count.items():
            result.extend([char] * counter)         
        return result