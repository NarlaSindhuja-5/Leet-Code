class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findPSE(heights):
            n=len(heights)
            stack=[]
            ans=[0]*n
            for i in range(0,n):
                while(len(stack)!=0 and heights[stack[-1]]>heights[i]):
                    stack.pop()
                if(len(stack)==0):
                    ans[i]=-1
                else:
                    ans[i]=stack[-1]
                stack.append(i)
            return ans
        def findNSE(heights):
            n=len(heights)
            stack=[]
            ans=[0]*n
            for i in range(n-1,-1,-1):
                while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
                    stack.pop()
                if(len(stack)==0):
                    ans[i]=n
                else:
                    ans[i]=stack[-1]
                stack.append(i)
            return ans
        n=len(heights)
        pse=findPSE(heights)
        nse=findNSE(heights)
        Area=0
        MaxArea=0
        for i in range(0,n):
            Area=heights[i]*(nse[i]-pse[i]-1)
            MaxArea=max(Area,MaxArea)
        return MaxArea
        