def right_rota(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n - 2, -1,-1):
        arr[i +1] = arr[i]
    arr[0] = temp
    print(arr)

def main():
    arr = list(map(int, input().split()))
    right_rota(arr)

main()