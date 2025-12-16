class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        v=0
        for num in nums:
            if c==0:
                v=num
            if num==v:
                c+=1
            else:
                c-=1
        return v
        