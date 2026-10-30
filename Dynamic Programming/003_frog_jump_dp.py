# recurson
class Solution:
    def solution(self, index, height):
        if index == 0:
            return 0

        jump1 = self.solution(index - 1,height) + abs(height[index] - height[index - 1])

        if index > 1:
            jump2 = self.solution(index - 2,height) + abs(height[index] - height[index - 2])
        else:
            jump2 = float("inf")
        return min(jump1, jump2)

    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height)

        return self.solution(n - 1, height)


###################################################################
# memoization

class Solution:
    def solution(self, index, height,dp):
        #if index == 0:
        #   return 0
        if dp[index] != -1:
            return dp[index]
        jump1 = self.solution(index - 1,height,dp) + abs(height[index] - height[index - 1])

        if index > 1:
            jump2 = self.solution(index - 2,height,dp) + abs(height[index] - height[index - 2])
        else:
            jump2 = float("inf")
        dp[index]  = min(jump1, jump2)
        return dp[index]

    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height)
        dp = [-1]*n
        dp[0] = 0
        return self.solution(n - 1, height, dp)

####################################################
#memorization bottom up
class Solution:

    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height)
        dp = [-1]*n
        dp[0] = 0
        return self.solution(n, height, dp)
    def solution(self, n, height,dp):
        for index in range(1, n):
            jump1 = dp[index-1]+ abs(height[index] - height[index - 1])

            if index > 1:
                jump2 = dp[index - 2] + abs(height[index] - height[index - 2])
            else:
                jump2 = float("inf")
            dp[index]  = min(jump1, jump2)
            
    
        return dp[n-1]

##########################################################################


class Solution:

    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height)
        return self.solution(n, height)
    def solution(self, n, height):
        prev = 0
        prev2 = float("inf")
        for index in range(1, n):
            jump1 = prev + abs(height[index] - height[index - 1])

            if index > 1:
                jump2 = prev2 + abs(height[index] - height[index - 2])
            else:
                jump2 = float("inf")
            curr = min(jump1, jump2)
            prev2 = prev
            prev = curr

        return prev

