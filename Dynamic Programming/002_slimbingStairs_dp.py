

# 1. recurssion

def recurtion(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    ans = recurtion(n-1) + recurtion(n-2)
    return ans

#print(recurtion(1))

# memo top  down
n = int(input())
dp = [-1] * (n)
def memo(n, dp):
    if n ==1:
        return 1
    if n ==2 :
        return 2
    if dp[n] != -1:
        return dp[n]
    ans = memo(n-1,dp) + memo(n-2,dp)
    return ans

#print(memo(n, dp))


# tabularixation


prev = 2
prev2 = 1

for i in range(2, n):
    curr = prev + prev2
    prev2 = prev
    prev = curr

print(prev)
    