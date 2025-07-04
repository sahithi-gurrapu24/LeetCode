class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dic={}
       for i in range(len(nums)):
         dic[nums[i]]=i
       for i in range(len(nums)):
        a=target-nums[i]
        if a in dic and dic[a]!=i:
            return [i,dic[a]]


        