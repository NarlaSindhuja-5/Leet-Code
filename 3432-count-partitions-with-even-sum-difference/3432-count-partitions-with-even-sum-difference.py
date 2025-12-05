
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum=0
        partitions=0
        left_sum=0
        for i in nums:
            total_sum+=i
        for i in range(len(nums) - 1):
            left_sum += nums[i]             
            right_sum = total_sum - left_sum
            if left_sum%2 == right_sum%2:
                partitions+=1
        return partitions


        