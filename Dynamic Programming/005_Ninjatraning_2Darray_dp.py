class Solution:
    def solve(self, day, last,mat):
        if day == 0:
            maxi = 0
            for i in range(0,3):
                if i != last:
                    maxi = max(maxi, mat[day][i])
            return maxi
        maxi = 0
        for i in range(0,3):
            if i != last:
                points = mat[day][i] + self.solve(day-1, i, mat)
                maxi = max(maxi, points )
                
        return maxi
            
    def maximumPoints(self, mat):
        n = len(mat)
        a = self.solve(n-1, 3,mat)
        return a
        
###########################################


class Solution:

    def solve(self, day, last, mat, dp):

        # STEP 1: Base case
        if day == 0:
            maxi = 0

            for i in range(3):

                # We cannot perform the last activity again
                if i != last:

                    maxi = max(maxi, mat[day][i])

            return maxi

        # STEP 2: Check if answer is already calculated
        if dp[day][last] != -1:
            return dp[day][last]

        maxi = 0

        # STEP 3: Try all three activities
        for i in range(3):

            if i != last:

                # Current activity points + previous days' maximum points
                points = mat[day][i] + self.solve(day-1, i, mat, dp)

                # Store the maximum answer
                maxi = max(maxi, points)

        # STEP 4: Store the calculated answer
        dp[day][last] = maxi

        # STEP 5: Return the answer
        return dp[day][last]

    def maximumPoints(self, mat):

        n = len(mat)

        # DP array: n rows and 4 columns
        dp = [[-1, -1, -1, -1] for _ in range(n)]

        return self.solve(n-1, 3, mat, dp)



    ##################################




    class Solution:
    def solve(self,mat, dp,n):
        for day in  range(1, n):
            for last in range(0,4):
                maxi =0
                for i in range(0,3):
                    if i != last:
                        maxi = max(maxi, mat[day][i] + dp[day-1][i])
                dp[day][last] = maxi
        return dp[n-1][3]
            
    def maximumPoints(self, mat):
        n = len(mat)
        dp = [[-1, -1, -1, -1] for _ in range(n)]
        dp[0][0] = max(mat[0][1], mat[0][2])
        dp[0][1] = max(mat[0][0], mat[0][2])
        dp[0][2] = max(mat[0][0], mat[0][1])
        dp[0][3] = max(mat[0][0], mat[0][1], mat[0][2])
        a = self.solve(mat, dp, n)
        return a




        #####################################################3


        