class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        unique = set()

        for word in words:
            slang = ""
            for ch in word:
                slang += morse[ord(ch) - ord('a')]
            unique.add(slang)
        return len(unique)