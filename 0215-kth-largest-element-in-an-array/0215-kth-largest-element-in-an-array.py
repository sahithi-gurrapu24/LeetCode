import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        v= heapq.nlargest(k,nums)
        return v[-1]
        