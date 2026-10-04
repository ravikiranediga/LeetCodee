class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count=0
        current_count=0
        n=len(nums)

        for num in nums:
            if num==1:
                current_count+=1
            else:
                max_count=max(max_count,current_count)
                current_count =0
        return max(max_count,current_count)