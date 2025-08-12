class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(c.lower() for c in s if c.isalnum())
        left=0
        right=len(string)-1
        while left < right:
            if string[left] !=string[right]:
                return False
            right-=1
            left+=1
        return True