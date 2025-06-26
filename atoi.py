# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

class Solution:
    def myAtoi(self, s: str) -> int:
        i,n = 0, len(s)
        sign = 1
        result = 0
        while i < n and s[i] == " ":
            i+= 1
        if i<n and s[i] == "-" or s[i] == "+":
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
            i += 1
        return result * sign
    
s = Solution()
print(s.myAtoi(" -042"))
