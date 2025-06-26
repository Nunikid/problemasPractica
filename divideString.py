#A string s can be partitioned into groups of size k, x fills the rest of the string if there are no more chars

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        strings = []
        for i in range(0,len(s),k):
            strings.append(s[i:i+k])
        strings[-1] += fill * (k - len(strings[-1]))
        return strings

s = Solution()
print(s.divideString("abcdefghij",3,"x"))