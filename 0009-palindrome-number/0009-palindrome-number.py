class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        ans=(s==s[::-1])
        if(ans):
            return True
        else:
            return False

        