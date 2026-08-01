def linear_search(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i
    return -1

def main():
    array = list(map(int, input().split()))
    a = int(input())
    b = linear_search(array, a)
    print(b)
main()