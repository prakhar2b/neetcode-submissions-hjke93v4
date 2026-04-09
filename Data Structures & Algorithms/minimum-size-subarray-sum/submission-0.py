class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        min_length = 9999999
        count_ = 0
        sum_ = 0
        while r<len(nums):
            sum_ += nums[r]
            print(r, sum_, r-l+1)
            if sum_ < target:
                r = r+1
            else:
                while sum_ >= target:
                    count_ += 1
                    min_length = min(min_length, r-l+1)
                    print(r, sum_, r-l+1)
                    sum_ -= nums[l]
                    l = l+1
                r = r+1

        if count_:
            return min_length
        
        return 0