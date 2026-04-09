class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_ = 0
        l,r = 0, k-1

        sum_ = sum(arr[i] for i in range(k))
        if sum_/k >= threshold:
            count_ += 1

        r = r+1
        while r<len(arr):
            sum_ = sum_ - arr[l] + arr[r]
            l, r = l+1, r+1
            if sum_/k >= threshold:
                count_ += 1

        return count_

