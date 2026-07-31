class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []

        for i in range(len(heights) - 1):
            j = i + 1
            end = len(heights) - 1

            while j <= end:
                areas.append(min(heights[i], heights[j]) * (j - i))
                j += 1
        
        return max(areas)