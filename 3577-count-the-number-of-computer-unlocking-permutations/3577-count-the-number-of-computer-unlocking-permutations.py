class Solution:
    def countPermutations(self, c: List[int]) -> int:
        MOD=10**9+7
        n=len(c)

        first=c[0]
        for x in c[1:]:
            if x<=first:
                return 0

        ans=1
        for i in range(2, n):
            ans=(ans*i)%MOD

        return ans
