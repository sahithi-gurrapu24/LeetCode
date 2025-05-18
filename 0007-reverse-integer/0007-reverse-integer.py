class Solution:
    def reverse(self, x: int) -> int:
        min=-(2**31)
        max=(2**31)-1
        s=str(x)
        ans=0
        if s[0]=='-':
            s=s[1:]
            ans= -int(s[::-1])
        else:
            ans=int(s[::-1])

       
        if ans>min and ans<max:
            return ans
        return 0
        