class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lt=0
        s=sum(nums)
        for i in range(len(nums)):
            rt=s-lt-nums[i]
            if rt==lt:
                return i
            lt+=nums[i]
        return -1
        