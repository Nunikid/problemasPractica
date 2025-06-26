#A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]
        
        left, count, ans = 1, 0, 0
        while count < n:
            right = left * 10
            # 0 odd, 1 even
            for op in [0, 1]:
                for i in range(left, right):
                    if count == n:
                        break
                    combined = i
                    print("first combined", i)
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        print(combined,"is valid")
                        count += 1
                        ans += combined
            left = right
        
        return ans


s = Solution()
print(s.kMirror(2,9))


