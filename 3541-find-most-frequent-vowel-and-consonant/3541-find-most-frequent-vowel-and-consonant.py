class Solution:
    def maxFreqSum(self, s: str) -> int:
        v1={}
        v2={}
        sv=set('aeiou')
        for i in s:
            if i in sv:
                v1[i]=v1.get(i,0)+1
            else:
             v2[i]=v2.get(i,0)+1
        max1=max(v1.values())if v1 else 0
        max2=max(v2.values())if v2 else 0
        return max1+max2
        