# Revertir un numero entero, si el numero es mayor que 32 bits, regresar 0

class Solution:
    def reverse1(self, x: int) -> int:
        reverse_int = 0
        revArray = list(map(int,str(abs(x))))
        revArray.reverse()
        for i in range(len(revArray)):
            reverse_int += revArray[i] * (10**(len(revArray) - 1 - i))
        if (x < 0):
            reverse_int = reverse_int * -1
        bitlength = reverse_int.bit_length()
        if bitlength > 31:
            return 0
        return reverse_int
    
    # Without bit_length
    def reverse2(self, x: int) -> int:
        reverse_int = 0
        revArray = list(map(int,str(abs(x))))
        revArray.reverse()
        for i in range(len(revArray)):
            reverse_int += revArray[i] * (10**(len(revArray) - 1 - i))
        if (x < 0):
            reverse_int = reverse_int * -1
        if reverse_int > 2 ** 31 or reverse_int < -2 ** 31 -1: 
            return 0
        return reverse_int
    
    # OPTIMAL
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev

s = Solution()
print(s.reverse1(1563847412))
