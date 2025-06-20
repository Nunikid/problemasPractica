import numpy as np
from collections import deque

class Solution:
    ##BRUTE FORCE
    def maxDistanceBF(self, s: str, k: int) -> int:
        maxDistance = 0
        currentPosition = np.array([0,0])
        movementsLeft = k
        movString = ""
        directions = {"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
        currentPath = set()
        for i in range(len(s)):
            if s[i] in directions:
                if s[i] == "S" and "N" in currentPath and movementsLeft > 0:
                    movString += "N"
                    movementsLeft -= 1
                elif s[i] == "N" and "S" in currentPath and movementsLeft > 0:
                    movString += "S"
                    movementsLeft -= 1
                elif s[i] == "E" and "W" in currentPath and movementsLeft > 0:
                    movString += "W"
                    movementsLeft -= 1
                elif s[i] == "W" and "E" in currentPath and movementsLeft > 0:
                    movString += "E"
                    movementsLeft -= 1
                else:
                    movString += s[i]
                currentPath.add(movString[i])
                print(movString)
                #Calculate current position
                currentPosition += np.array(directions[movString[i]])

            #MaxDistance
            maxDistance = max(maxDistance,abs(currentPosition[0]) + abs(currentPosition[1]))
        print(currentPosition)
        print(maxDistance)
        return maxDistance
    
    # OPTIMAL
    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans



s = Solution()
print(s.maxDistance("NSWWEW",3))
