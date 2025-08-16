class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        win=nums[:k]
        sumvalue=sum(win)
        maxsum=sumvalue
        for i in range(k,len(nums)):
            sumvalue +=nums[i]-nums[i-k]
            maxsum=max(sumvalue,maxsum)
        return maxsum/k


        