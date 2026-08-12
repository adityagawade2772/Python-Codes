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


def better(arr): # O(n + nlogn)
    arr.sort() # tc -> O(nlogn)
    last_small= "-inf"
    count= 0
    n = len(arr)
    longest= 0
    for i in range(0,n): #tc O(n)
        num = arr[i]
        if num-1== last_small:
            count += 1
            last_small= num
        else:
            count = 1 
            last_small = num
        longest= max(longest, count)

    return longest


def optimal(arr):
    my_set= set()
    n = len(arr)
    for i in range(0, n):
        my_set.add(arr[i])
        

def main():
    n = list(map(int, input().split()))
    a = better(n)
    print(a)
main()
