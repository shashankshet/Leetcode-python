class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        maxWater = 0
        while(i<j):
            diff = j-i
            minH = min(height[i],height[j])
            CurmaxWater = diff* minH
            maxWater = max(maxWater,CurmaxWater)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxWater
