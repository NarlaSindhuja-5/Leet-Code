class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        penalty=customers.count('Y')
        min_penalty=penalty
        best_hour=0
        for i in range(n):
            if customers[i]=='Y':
                penalty-=1
            else:
                penalty+=1
            if penalty<min_penalty:
                min_penalty=penalty
                best_hour=i+1
        return best_hour

        