"""
Similar to Coin Change
We have to return all the possible combinations which add up to 1
Brute Force Recursion : choose/not choose for each node
At each node, we maintain the current sum and list of chosen elements

We have to ensure that the action of adding a child to the list is backtracked before the parent processing begins after the child(from the recursion stack)
current sum, path will be local variables
current sum will be passed by value so we dont have to subtract the value when we go back to the parent node

Condition for end of recursion? amount = 0 or negative



"""
# 0/1 recursion with backtracking 
# TC Exponential =  (Target/min(nums))+len(nums)
# SC Recursive stack space

class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], targetSum: int) -> List[List[int]]:
        
        if len(candidates)==0 or candidates is None :
            return []
        i = 0
        path = []
        self.helper(candidates, targetSum, i, path)
        return self.result
    
    def helper(self, candidates, targetSum, i, path):
        #base
        if targetSum<0 or i>=len(candidates):
            return
        if targetSum==0:
            self.result.append(path[:])
            #print(result)
            return
        #logic
        
        #action
        #case 0 no choose
        self.helper(candidates, targetSum, i+1, path)
        
        
        #case 1 choose
        path.append(candidates[i])
        print(path)
        self.helper(candidates,targetSum - candidates[i], i, path)
        #recursion
        
        #backtrack
        path.pop()
        

        
        