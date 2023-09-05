def maxArea(self, height):
    max_water = 0
    left, right = 0, len(height)-1
    while left < right:
        water = min(height[left], height[right]) * (right-left)
        max_water = max(water, max_water)
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    return max_water

