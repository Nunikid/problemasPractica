## Dados 4 numeros, regresar el numero de combinaciones que dan una hora valida
from itertools import permutations

class Solution(object):
    def validHour(self, A:int, B:int, C:int, D:int)-> int:
        count = 0
        numbers = [A,B,C,D]
        perm = permutations(numbers)
        for i in perm:
            if i[0] * 10 + i[1] < 24 and i[2] * 10 + i[3] < 60:
                print(str(i[0])+str(i[1])+":"+str(i[2])+str(i[3]))
                count += 1
        return count
s = Solution()
print(s.validHour(2,7,2,3))

