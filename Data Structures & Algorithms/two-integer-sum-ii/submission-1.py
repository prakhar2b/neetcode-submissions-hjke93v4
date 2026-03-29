class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i,num in enumerate(numbers):
            comp_ = target - num
            l, r = i+1, len(numbers) - 1
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == comp_:
                    return [i+1, mid+1]
                elif numbers[mid] < comp_:
                    l = mid + 1
                else:
                    r = mid - 1

        return []

