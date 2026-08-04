def two_sum(target, arr):
    n = len(arr)
    hash_map = {}

    for i in range (0, n):
        remening = target - arr[i]
        if remening in hash_map:
            return hash_map[remening], i
        hash_map[arr[i]] = i

def main():
    n = list(map(int, input().split()))
    m = int(input())
    a =two_sum(m, n)
    print(a)

main()


    