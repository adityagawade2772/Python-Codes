# 1,  recurtion
class Solution:
    def solve(self, index,nums):
        if index<0:
            return 0
        if index == 0:
            return nums[index]
        pick = nums[index] + self.solve(index-2, nums)
        not_pick = 0 + self.solve(index-1, nums)
        return max(pick, not_pick)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        a = self.solve(n-1, nums)
        return a


##########################################

class Solution:
    def solve(self, index,nums,dp):
        if index<0:
            return 0
        if index == 0:
            return nums[index]
        if dp[index] != -1:
            return dp[index]
        
        
        pick = nums[index] + self.solve(index-2, nums,dp)
        not_pick = 0 + self.solve(index-1, nums,dp)
        dp[index] = max(pick, not_pick)
        return dp[index]



    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        a = self.solve(n-1, nums, dp)
        return a


######################################

class Solution:
    def solve(self,nums,dp,n):
        
        
        for index in range(1,n):

        
            if index > 1:
                pick = nums[index]+ dp[index-2]
            else: 
                pick =nums[index]
            not_pick = 0 + dp[index-1]
            dp[index] = max(pick, not_pick)
        return dp[n-1]



    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        a = self.solve(nums, dp, n)
        return a



###########################################

class Solution:
    def solve(self,nums,dp,n):
        prev = nums[0]
        prev2 = 0

        for index in range(1,n):
            
            
            if index > 1:
                pick = nums[index]+ prev2
            else: 
                pick =nums[index]
            not_pick = 0 + prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr
            
        return prev



    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        a = self.solve(nums, dp, n)
        return a
