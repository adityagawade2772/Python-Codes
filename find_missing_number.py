# O(n^2) time compllexity [4, 1, 3, 5, 0, 6]
def find(arr):
    n = len(arr)
    for i in range(0, n+1): # tc -> O(n)
        if i not in arr: # tc -> O(n)
            return i


def solution(arr):# tc -> O(3n)
    n = len(arr)
    freq={}
    for i in range(0, n+1):  # tc -> O(n)
        freq[i] = 0

    for i in arr: # tc -> O(n)
        freq[i] += 1

    for k, v in freq.items(): # tc -> O(n)
        if v == 0:
            return k


def optimal(arr):
    n = len(arr)
    return ((n *(n+1))/ 2)- sum(arr)



def main():
    a = list(map(int, input().split()))
    b = optimal(a)
    print(b)

main()