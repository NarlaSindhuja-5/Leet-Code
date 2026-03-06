class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero=False
        for i in s:
            if i=='0':
                seen_zero=True
            elif seen_zero and i=='1':
                return False
        return True
        