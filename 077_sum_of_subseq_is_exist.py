def solve(index, sum, subset, nums, k, result):
    if sum == k:
        result.append(subset.copy())
        return True
    
    if sum > k:
        return False
    
    if index > len(nums):
        return False
    
    subset.append(nums[index])
    sum += nums[index]
    pick = solve(index+1, sum, subset, nums,k, result)
    if pick == True:
        return True
    
    e = subset.pop()
    sum -= e

    not_pick = solve(index+1, sum,subset,nums,k,result)
    return not_pick
def main():
    n = list(map(int, input().split()))
    k = int(input("enter taeget:" ))
    a =solve(0,0,[],n,k,[])
    print(a)

main()

