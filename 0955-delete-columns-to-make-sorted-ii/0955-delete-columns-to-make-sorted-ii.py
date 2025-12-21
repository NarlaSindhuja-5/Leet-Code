class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        deleted=0
        sorted_rows=[False]*(n-1)
        for col in range(m):
            bad=False
            for row in range(n-1):
                if not sorted_rows[row] and strs[row][col]>strs[row+1][col]:
                    bad=True
                    break
            if bad:
                deleted+=1
            else:
                for row in range(n-1):
                    if strs[row][col]<strs[row+1][col]:
                        sorted_rows[row]=True
        return deleted

        