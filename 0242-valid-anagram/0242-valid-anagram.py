class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cS={}
        cT={}
        for i in s:
            cS[i]=cS.get('i',0)+1
        for i in t:
            cT[i]=cT.get('i',0)+1
        return cS==cT