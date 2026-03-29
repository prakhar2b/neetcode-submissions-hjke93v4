class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        trips = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0-nums[i]

            l = i+1
            r = len(nums) - 1

            while l<r:
                sum_ = nums[l] + nums[r]
                if sum_ > target:
                    r = r-1
                elif sum_ < target:
                    l = l+1
                else:
                    trips.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    r = r-1
                    while nums[l] == nums[l-1] and l<r:
                        l=l+1
            
        return trips

