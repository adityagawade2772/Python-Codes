def main():
    array = list(map(int, input().split()))
    n = len(array)
    for i in range(0, n-2):
        if array[i]>array[i+1]:
            return False

    return True




print(main())