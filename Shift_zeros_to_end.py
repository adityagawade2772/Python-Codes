# 1 2 0 0 5
def shift_zeros_to_end(arr):
    n = len(arr)
    temp = []
    for i in range(0, n):
        if arr[i] != 0:
            temp.append(arr[i]) # temp =[1 2 5]

    k = len(temp) # 3

    for i in range(0, k):
        arr[i] = temp[i] #[1 2 5 0 5]

    for i in range(k, n):
        arr[i] = 0
    print(arr)


def optimal(arr):
    if len(arr)==1:
        return
    i = 0
    while i < len(arr):
        if arr[i ] == 0:
            break

        i += 1
        if i == len(arr):
            return

    j = i+1
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1

        j+=1

    print(arr)    


def main():
    arra = list(map(int, input().split()))
    optimal(arra)

main()