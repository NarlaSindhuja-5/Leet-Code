class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = []
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seats.append(i)
        
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0
        
        ways = 1
        
        for i in range(2, len(seats), 2):
            left = seats[i - 1]
            right = seats[i]
            plants = right - left - 1
            ways = (ways * (plants + 1)) % MOD
        
        return ways
