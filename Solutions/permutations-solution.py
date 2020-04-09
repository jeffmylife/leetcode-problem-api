class Solution:
    def _permute(self, nums):
        return [[n] + p 
                for i,n in enumerate(nums)
                for p in _permute(nums[:i] + nums[i+1:])] or [[]]
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = Solution._permute(self,nums)
        return permutations
        
            
"""
First, I'll describe how i unsuccessfully approached the problem. 

I figured, "get permutations for nums by taking each number (n) in nums and get permutations for every other number (p) and append to n." Generally, this is actually a correct solution. I got the idea by thinking about how to compute factorials. 
I successfully generated the permutations but in a form that was so complicated, it would need recursion to parse the combinations. This is obviously because I was appending in the wrong manner. 
Here were some major problems with my solution: 
1) While correct about recursively calling on "other" numbers for all numbers, I used a return a "temporary list" that contained the permuted subset for "other" but I couldn't figure out how to add it back. This is similar to the solution above except that I didn't add to the parent number correctly. 
2) I had code that was constantly needing to be "unpacked"; this is related to first point. 

Another minor problem was I was swapping elements when the list got to size 2. My logic was that was where the permuting happened. It was actually unecessary. The permutation happens at the "splitting" step, where the function calls itself on the "other" numbers. 

e.g., for [1,2,3] the first calls on 1: 

# time = up to down 
permute([1,2,3])               <-- [1] + 
# 1 is the "n" in this case; [2,3] is the "other" list that is defined by the line 'nums[:i] + nums[i+1:]' 

permute([2,3])                 <-- [2] + 
# 2 is "n"; [3] is "other" 

permute([3])                   <-- [3] + 
# 3 is "n"; [] is "other" 

permute([]) returns [[]]       <-- []        base case 

permute([2])                   <-- [2] + 
# 2 is "n"; [] is "other" 

permute([]) returns [[]]       <-- []        base case 
 

-- Call order -->         <-- Return order-- 
permute([1,2,3]) + permute([2,3]) + permute([3]) + (permute([]))
permute([1,2,3]) + permute([2,3]) + (permute([3]) + [])
permute([1,2,3]) + (permute([2,3]) + [3])
(permute([1,2,3]) + [2,3]) 
[1,2,3]

-- Call order -->         <-- Return order-- 
permute([1,2,3]) + permute([2,3]) + permute([2]) + (permute([]))
permute([1,2,3]) + permute([2,3]) + (permute([2]) + [])
permute([1,2,3]) + (permute([2,3]) + [2])
(permute([1,2,3]) + [3,2]) 
[1,3,2]

Last, 

The solution is interesting because it does it in one line. Also, it handles the empty list elegantly. It's like saying "the only permutation of the empty list is the empty list in it's current position." Just like in the single-element list, there's only one way to arrange nothing (this is why 0! = 1 ). 

"""
