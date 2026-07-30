#input 1 2 2 4 4 5
#o/p  4
def remove_duplicates(arr):
    n = len(arr)
    if(n==1):
        return 1
    i = 0
    j= i + 1
    while j < n:
        if arr[j] != arr[i]:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
    return i+1

def main():
    n = list(map(int, input().split()))
    a = remove_duplicates(n)
    print(a)

main()

