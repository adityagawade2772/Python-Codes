def brout(arr): #O(n^2)
    n = len(arr)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1, n):
            if(arr[i]< arr[j]):
                max_profit = max(max_profit, arr[j]- arr[i])

    return max_profit

def optimal(prices):
    max_profit = 0
    min_price = float("inf")
    n = len(prices)
    for i in range(0,n):
        min_price = min(prices[i], min_price)
        max_profit = max(max_profit, prices[i]- min_price)

    return max_profit


def main():
    n = list(map(int, input().split()))
    a = optimal(n)
    print(a)
    
main()
