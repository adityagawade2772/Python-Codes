def find_subarray(arr):
    n = len(arr)
    maxi = float("-inf")

    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total = total + arr[j]
            maxi = max(maxi, total)

    return maxi
def optimal(arr):
    maxi = float("-inf")
    total = 0 
    n = len(arr)
    for i in range(0, n):
        total += arr[i]
        if (total <0):
            total = 0
        maxi = max(maxi, total)
    return maxi


def main():
    a = list(map(int, input().split()))
    b = optimal(a)
    print(b)

main()