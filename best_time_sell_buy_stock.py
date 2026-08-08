def brout(arr): #O(n^2)
    n = len(arr)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1, n):
            if(arr[i]< arr[j]):
                max_profit = max(max_profit, arr[j]- arr[i])

    return max_profit


def main():
    n = list(map(int, input().split()))
    a = brout(n)
    print(a)
    
main()
