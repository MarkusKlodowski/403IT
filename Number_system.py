class Solution:
    def average(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        avarage = sum(salary)/(len(salary))

        return(avarage)
#print(Solution.average(1, [4000,3000,1000,2000]))

class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        total = 1
        for i in range (0,len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
        if total < 0:
            for i in range(0,len(nums)):
                if nums[i] > 0 or nums[-1] < 0:                 
                    total = total / nums[i-1]
                    return(int(total))
        else:
            return(int(total))

print(Solution.maxStrength(1, [8,6,0,5,-4,-8,-4,9,-1,6,-4,8,-5]))