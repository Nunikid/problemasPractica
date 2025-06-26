#You are given a string word and an integer k.
# We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.
# Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.
# Return the minimum number of characters you need to delete to make word k-special.

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        map = {}
        res = len(word)
        for i in range(len(word)):
            if word[i] in map:
                map[word[i]] += 1
            else:
                map[word[i]] = 1
        print(map)

        # If a char occurence is greater than another num, delete the char that appears the least. 
        for i in map:
            deletions = 0
            for j in map:
                if map[i] > map[j]:
                    deletions += map[j]
                if map[j] > map[i] + k:
                    deletions += map[j] - (map[i]+k)
            res = min(res,deletions)
        return res

    
s = Solution()

print(s.minimumDeletions("aabaa",0))

        