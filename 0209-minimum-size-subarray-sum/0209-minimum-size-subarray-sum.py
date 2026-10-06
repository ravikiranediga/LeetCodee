class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans= float('inf')
        left=0
        n=len(nums)
        sum=0

        for right in range(n):
            sum+=nums[right]

            while sum >= target:
                ans=min(ans,right - left + 1)
                sum-=nums[left]

                left+=1

        return 0 if ans == float('inf') else ans