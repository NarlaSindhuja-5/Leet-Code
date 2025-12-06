class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        n=len(nums)
        p=[0]*(n+1)
        p[0]=1
        for i in range(n):
            current_min=float('inf')
            current_max=float('-inf')
            for j in range(i,-1,-1):
                current_min = min(current_min, nums[j])
                current_max = max(current_max, nums[j])
                if current_max-current_min<=k:
                    p[i+1]=(p[i+1]+p[j])%mod
                else:
                    break
        return p[n]


