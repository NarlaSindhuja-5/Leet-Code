from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1
        
        minQ = deque()
        maxQ = deque()
        left = 0
        
        for right in range(n):
            while minQ and nums[minQ[-1]] > nums[right]:
                minQ.pop()
            minQ.append(right)
            
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            maxQ.append(right)
            
            while nums[maxQ[0]] - nums[minQ[0]] > k:
                left += 1
                if minQ[0] < left:
                    minQ.popleft()
                if maxQ[0] < left:
                    maxQ.popleft()
            dp[right+1] = (pref[right] - (pref[left-1] if left > 0 else 0)) % MOD
            pref[right+1] = (pref[right] + dp[right+1]) % MOD
        
        return dp[n]
