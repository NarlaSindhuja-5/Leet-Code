class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        right = {}
        for value in nums:
            if value in right:
                right[value] += 1
            else:
                right[value] = 1

        left = {}
        answer = 0

        for j in range(n):
            right[nums[j]] -= 1
            target = nums[j] * 2

            if target in left:
                left_count = left[target]
            else:
                left_count = 0

            if target in right:
                right_count = right[target]
            else:
                right_count = 0

            answer = (answer + left_count * right_count) % mod

            if nums[j] in left:
                left[nums[j]] += 1
            else:
                left[nums[j]] = 1

        return answer
