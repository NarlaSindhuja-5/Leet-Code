class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        length=len(s.split()[-1])
        return length



        