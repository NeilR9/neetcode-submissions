class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights == 2:
            return 1 * min(heights[0], heights[1])
        left = 0
        right  = len(heights) - 1
        maxSum = 0
        while left < right:
            #print(f"Left Num: {heights[left]}")
            #print(f"Right Num: {heights[right]}")
            #print(f"New Sum: {(right - left) * min(heights[left], heights[right])}")
            if ((right - left) * min(heights[left], heights[right])) > maxSum:
                maxSum = ((right - left) * min(heights[left], heights[right]))
                #print(f"New Max Sum: {maxSum}")
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        return maxSum

        