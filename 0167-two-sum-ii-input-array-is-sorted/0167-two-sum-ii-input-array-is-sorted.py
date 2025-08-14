class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        while left <right:
            sumvalue=numbers[left]+numbers[right]
            if sumvalue==target:
                return [left+1,right+1]
            elif sumvalue>target:
                right-=1
            else:
                left+=1


        