class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash=set()
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash.add(nums[i])
            else:
                return True
        return False
        