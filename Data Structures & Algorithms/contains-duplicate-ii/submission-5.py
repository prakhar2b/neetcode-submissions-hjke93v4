class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        window = set()
        l,r = 0, 1
        window.add(nums[l])

        while r<len(nums):
            if nums[r] in window:
                print("here?",r,nums[r])
                return True
            else:
                window.add(nums[r])
                if r-l+1>k:
                    window.remove(nums[l])
                    l = l+1
                r= r+1

        return False


