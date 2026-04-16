class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        # Computing maxArea from left to right
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        print(stack)

        # Computing maxArea from right to left
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea