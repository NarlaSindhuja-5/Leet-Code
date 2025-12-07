class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total_numbers = high - low + 1
        if low % 2 == 1 or high % 2 == 1:
            return (total_numbers + 1) // 2
        else:
            return total_numbers // 2
