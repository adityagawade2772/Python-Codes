class Solution:
    def solve(self, index, total, nums, result):
        if index>= len(nums):
            result.append(total)
            return

        sum = total + nums[index]
        self.solve(index+1, sum,nums, result)
        sum = total
        self.solve(index+1, sum,nums, result)

    def main(self):
        nums = list(map(int,input().split()))
        result = []
        self.solve(0,0,nums,result)
        print(result)

    
Solution().main()

