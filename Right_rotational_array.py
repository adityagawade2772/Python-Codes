def right_rota(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n - 2, -1,-1):
        arr[i +1] = arr[i]
    arr[0] = temp
    print(arr)

# k times right rotataiom
def k_times(arr, k):
    n = len(arr)

    for _ in range (0 , k):
        e = arr.pop()
        arr.insert(0, e)

    print(arr)




def main():
    arr = list(map(int, input("Enter array ").split()))
    k = int(input("enter rotaions "))

    # right_rota(arr)
    k_times(arr, k)

main()