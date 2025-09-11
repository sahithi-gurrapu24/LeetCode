class Solution:
    def sortVowels(self, s: str) -> str:
        vow=set('aeiouAEIOU')
        v=[]
        for i in s:
            if i in vow:
                v.append(i)
        v.sort()
        t=[]
        vi=0
        for i in range(len(s)):
            if s[i] not in vow:
                t.append(s[i])
            else:
                t.append(v[vi])
                vi+=1 
        return "".join(t)









         
        