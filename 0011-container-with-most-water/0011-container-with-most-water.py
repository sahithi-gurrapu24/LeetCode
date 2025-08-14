class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        maxValue=0
        right=len(height)-1
        while left<right:
            Value=min(height[left],height[right])*(right-left)
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
            maxValue=max(Value,maxValue)
        return maxValue

        