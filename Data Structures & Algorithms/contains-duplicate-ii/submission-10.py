class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        if k<1:
            return False
        
        w = k+1
        window = set()
        l = 0

        for r in range(len(nums)):
            
            if r-l+1 > w:
                window.remove(nums[l])
                l = l+1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r = r+1

        return False

        """
        window = set()
        l,r = 0, 1
        window.add(nums[l])

        while r<len(nums):
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
                if r-l+1>k:
                    window.remove(nums[l])
                    l = l+1
                r= r+1

        return False"""


