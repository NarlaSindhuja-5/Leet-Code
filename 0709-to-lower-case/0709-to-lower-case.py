class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in s:
            if(ord(i)>=65 and ord(i)<=90):
                return s.lower()
        return s
        
        
        