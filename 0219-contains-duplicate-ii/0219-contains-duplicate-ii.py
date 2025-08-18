class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w=set()
        for i,num in enumerate(nums):
            if num in w:
                return True
            w.add(num)
            if len(w)>k:
                w.remove(nums[i-k])
        return False

        