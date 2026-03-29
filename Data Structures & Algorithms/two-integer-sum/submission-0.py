class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store: { value: index }
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                # We found the pair! Return [smaller_index, larger_index]
                return [prevMap[diff], i]
            
            # Store current number and its index for future reference
            prevMap[n] = i
            