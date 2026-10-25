def solve(index, subset,nums,result):
    if (index >= len(nums)):
        result.append(subset.copy)
        return
    
    subset.append(nums[index])
    solve(index+1,subset,nums,result)
    subset.pop()
    solve(index+1,subset, nums,result)
    


def main():
    nums = list(map(int, input().split()))
    result= []
    solve(0,[],nums,result)
    print(result)

main()



    