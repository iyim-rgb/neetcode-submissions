class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 

        for i in range(len(heights) - 1):
            j = i + 1
            end = len(heights) - 1

            while j <= end:
                area = min(heights[i], heights[j]) * (j - i)
                max_area = max(max_area, area)
                j += 1
        
        return max_area