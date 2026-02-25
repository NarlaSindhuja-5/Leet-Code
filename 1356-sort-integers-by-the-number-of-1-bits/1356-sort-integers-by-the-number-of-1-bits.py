class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(n):
            return bin(n).count('1')
        arr.sort(key=lambda x: (countBits(x), x))
        return arr
        