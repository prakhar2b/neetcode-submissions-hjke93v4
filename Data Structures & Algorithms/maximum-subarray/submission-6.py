class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0,1
        max_so_far = nums[0]
        cur_sum = nums[0]
        while r<len(nums):
            cur_sum = cur_sum + nums[r]
            print('cur_sum', cur_sum)
            if nums[r] >= cur_sum:
                l = r
                r = r+1
                max_so_far = max(max_so_far,nums[l])
                cur_sum = nums[l]
                print('updated cur sum', cur_sum)
            else:
                max_so_far = max(max_so_far,cur_sum)
                r = r+1
            print("max_", max_so_far)

        return max_so_far