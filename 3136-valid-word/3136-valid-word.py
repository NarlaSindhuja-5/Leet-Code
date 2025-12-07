class Solution:
    def isValid(self, word: str) -> bool:
        vowel_count = 0
        consonent_count = 0
        
        for ch in word:
            if ch.isalpha():
                if ch.lower() in ['a','e','i','o','u']:
                    vowel_count += 1
                else:
                    consonent_count += 1
            elif ch.isdigit():
                continue
            else:
                return False

        if vowel_count >= 1 and consonent_count >= 1 and len(word) >= 3:
            return True
        return False
