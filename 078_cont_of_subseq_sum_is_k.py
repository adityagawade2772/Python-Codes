def solve(index, sum, nums, k):
    if sum ==k:
        return 1
    
    if index >= len(nums):
        return 0
    
    if sum > k:
        return 0
    
    sum += nums[index]
    pick =solve(index+1, sum, nums,k)
    sum -= nums[index]
    not_pick = solve(index+1, sum, nums,k)
    return pick + not_pick

def main():
    n = list(map(int, input().split()))
    k = int(input())
    a = solve(0,0,n,k)
    print(a)

main()
