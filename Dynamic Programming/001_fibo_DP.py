# ============================================================
#              DYNAMIC PROGRAMMING - FIBONACCI
# ============================================================

# 1) RECURSION (TOP-DOWN)
# Time Complexity: O(2^n)
# Space Complexity: O(n) - Recursion Stack Space


# 2) MEMOIZATION (TOP-DOWN DP)
# Time Complexity: O(n)
# Space Complexity: O(n) + O(n)
#                  Stack Space + DP Array


# 3) TABULATION (BOTTOM-UP DP)
# Time Complexity: O(n)
# Space Complexity: O(n) - DP Array


# 4) TABULATION (SPACE OPTIMIZATION)
# Time Complexity: O(n)
# Space Complexity: O(1) - Constant Space

# ============================================================
# APPROACH:
# Recursion -> Memoization -> Tabulation -> Space Optimization
# ============================================================\


# 1)Recursion (Top-Down Approach)

def recurtion(n):
    # Base case
    if n==1:
        return 1
    if n == 0:
        return 0

    # Recursive calls
    # Same subproblems are calculated multiple times
    return recurtion(n-1) + recurtion(n-2)

# Time Complexity: O(2^n)
# Space Complexity: O(n) - Recursion stack space


# 2) Memorization(Top-Down Approach)
def fib(n, dp):
    # Base cases
    if n <= 1:
        return n

    # If answer is already calculated, return it
    if dp[n] != -1:
        return dp[n]

    # Calculate and store the answer
    dp[n] = fib(n-1, dp) + fib(n-2, dp)

    return dp[n]


n = 5
dp = [-1] * (n + 1)
#print(fib(n, dp))

# Time Complexity: O(n)
# Space Complexity: O(n) + O(n)
# O(n) for recursion stack + O(n) for DP array

# 3) Tabulatiom(BottomUp)

def fib(n):
    # Create DP array
    dp = [0] * (n + 1)

    # Initialize base cases
    dp[0] = 0
    if n >= 1:
        dp[1] = 1

    # Build the answer from bottom to top
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


#print(fib(5))

# Time Complexity: O(n)
# Space Complexity: O(n) - DP array




# 4) Space Optimization (bottom up)
def fib(n):
    # Base cases
    if n <= 1:
        return n

    # Store only the previous two Fibonacci numbers
    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        # Calculate current Fibonacci number
        curr = prev1 + prev2

        # Update previous values
        prev2 = prev1
        prev1 = curr

    return prev1


print(fib(5))

# Time Complexity: O(n)
# Space Complexity: O(1) - Only 3 variables
