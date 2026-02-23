class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        if n<k:
            return False
        seen=set()
        for i in range(n-k+1):
            seen.add(s[i:i+k])
        total_codes=2**k
        return len(seen)==total_codes
        