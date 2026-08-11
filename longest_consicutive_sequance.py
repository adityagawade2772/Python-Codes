def brut(arr):
    n = len(arr)
    max_count = 0

    for i in range(0,n):
        count = 1
        num = arr[i]
        while num + 1 in arr:
            count += 1
            num += 1

        max_count = max(max_count, count)

    return max_count



def main():
    n = list(map(int, input().split()))
    a = brut(n)
    print(a)
main()
