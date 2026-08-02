def max_strick(arr):
    count= 0
    max_coutn= 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            max_coutn= max(max_coutn, count)
            count = 0

    return max(count, max_coutn)

def main():
    n = list(map(int, input().split()))
    a =  max_strick(n)
    print(a)

main()