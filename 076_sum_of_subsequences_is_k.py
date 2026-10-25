#  code and debug video no 76

def solve(index, subseq, total, k, nums, result):
    if total == k:
        result.append(subseq.copy())
        return
    
    if total > k:
        return
    
    if index>= len(nums):
        return
    
    subseq.append(nums[index])
    total += nums[index]
    solve(index+1,subseq,total,k,nums,result)
    e = subseq.pop()
    total-= e
    solve(index+1,subseq,total,k,nums,result)

def main():
    nums = list(map(int,input().split()))
    k = int(input())
    result = []
    solve(0,[],0,k,nums,result)
    print(result)

main()



    

