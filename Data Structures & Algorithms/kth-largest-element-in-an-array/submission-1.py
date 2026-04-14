class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max-heap
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            el_ = heapq.heappop(nums)

        return -1*el_