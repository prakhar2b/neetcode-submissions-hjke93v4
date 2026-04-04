class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_area = 0
        while l<r:
            area_ = min(heights[l],heights[r]) * (r-l)
            print(area_)
            max_area = max(max_area, area_)

            if heights[l] <= heights[r]:
                l = l+1
            else:
                r = r-1

        return max_area