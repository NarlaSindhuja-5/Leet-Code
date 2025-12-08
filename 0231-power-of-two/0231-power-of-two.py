class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        x = 1
        while 2 ** x <= n:
            if n == 2 ** x:
                return True
            x += 1
        
        return False
