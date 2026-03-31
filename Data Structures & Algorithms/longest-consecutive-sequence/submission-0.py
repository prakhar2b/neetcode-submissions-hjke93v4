class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = {}
        max_so_far = 0
        for i,n in enumerate(nums):
            hset[n] = n

        for num in nums:
            if (num in hset) and (num-1  not in hset):
                print(num)
                # start of a sequence
                i = 1
                while num + i in hset:
                    i = i+1
                #print(num, i-1)
                max_so_far = max(max_so_far, hset[num + i-1] - hset[num] + 1)

        return max_so_far
        