class Solution:
    def _permute(self, nums):
        if len(nums) > 2: 
            tmp_lol = []
            loop_nums = list(nums)
            for i, _ in enumerate(loop_nums):
                tmp_nums = [nums[i]] + nums[:i] + nums[i + 1:] 
                tmp_lol.append(tmp_nums)
                sub_perms = Solution._permute(self, nums[:i] + nums[i + 1:])
                tmp_nums_r = [nums[i], *sub_perms]

                tmp_lol.append(tmp_nums_r)
            return tmp_lol
        
        elif len(nums) == 2:
            return [nums[1], nums[0]]
        elif len(nums) == 1: 
            return nums
        else:
            raise Exception("Major error")
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = Solution._permute(self,nums)
        return permutations
        
            
