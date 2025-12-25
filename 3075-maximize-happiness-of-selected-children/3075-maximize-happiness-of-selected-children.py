class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total=0
        for i in range(k):
            value=happiness[i]-i
            if value>0:
                total+=value
        return total
        