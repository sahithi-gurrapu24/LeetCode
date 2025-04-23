
#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        if x < 0:
#            return False

#        original = x
#        reversed_num = 0
#        while x > 0:
#            digit = x % 10
#            # Check for overflow
#            if reversed_num > (2**31 - 1 - digit) // 10:
#                return False
#
#            reversed_num = reversed_num * 10 + digit
#            x //= 10
#
#        return original == reversed_num

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False
        