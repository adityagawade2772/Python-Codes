def solve(index, subset,nums,result):
    if (index >= len(nums)):
        result.append(subset.copy())
        # used .copy() bcoz if we don't used that it will only point to -> subset,
        # after some time if we made changes in subsert result also get changed,
        # so by using shallow copy it create new list
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



    