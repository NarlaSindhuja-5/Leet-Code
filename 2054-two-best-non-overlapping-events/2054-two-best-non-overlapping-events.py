from bisect import bisect_left
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        from bisect import bisect_left
        events.sort()
        n=len(events)
        start_times=[]
        for e in events:
            start_times.append(e[0])
        suffix_max=[0]*n
        suffix_max[-1]=events[-1][2]
        for i in range(n-2,-1,-1):
            suffix_max[i]=max(suffix_max[i+1],events[i][2])
        ans=0
        for i in range(n):
            start,end,value=events[i]
            ans=max(ans,value)
            next_index=bisect_left(start_times,end+1)
            if next_index<n:
                ans=max(ans,value+suffix_max[next_index])
        return ans

        
        