class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        if(len(nums))==0:
            return[-1,-1]
        
        lower=self.lower_bound(nums,target)
        upper=self.upper_bound(nums,target)
        if lower==len(nums) or lower==-1 or nums[lower]!=target:
            return[-1,-1]
        return[lower,upper-1]

    def lower_bound(self,nums,target):
        left=0
        right=len(nums)-1
        ans=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
    def upper_bound(self,nums,target):
        left=0
        right=len(nums)-1
        ans=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
        
        