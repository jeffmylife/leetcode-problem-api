class Solution:
    def _permute(self, nums):
        return [[n] + p for i,n in enumerate(nums)
        for p in _permute(nums[:i] or nums[i+1:])] + [[]]
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = Solution._permute(self,nums)
        return permutations
        
            
