class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        j = 0
        k = len(heights) - 1

        while j < k:
            area = min(heights[j], heights[k]) * (k - j)
            max_area = max(max_area, area)
            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1
        
        return max_area