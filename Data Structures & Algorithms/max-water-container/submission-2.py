class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights == 2:
            return 1 * min(heights[0], heights[1])
        left = 0
        right  = len(heights) - 1
        maxSum = 0
        while left < right:
            if ((right - left) * min(heights[left], heights[right])) > maxSum:
                maxSum = ((right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        return maxSum

        